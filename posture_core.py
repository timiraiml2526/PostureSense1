import cv2
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import streamlit as st

@st.cache_resource
def load_detector():
    options = vision.PoseLandmarkerOptions(
        base_options=python.BaseOptions(model_asset_path="pose_landmarker_lite.task"),
        running_mode=vision.RunningMode.IMAGE,
    )
    return vision.PoseLandmarker.create_from_options(options)

detector = load_detector()

class PostureDetector:
    def process(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        result = detector.detect(mp_img)

        posture = "No Pose"

        if result.pose_landmarks:
            lms = result.pose_landmarks[0]
            left = lms[11]
            right = lms[12]

            diff = abs(left.y - right.y)

            if diff > 0.10:
                posture = "Bad"
                color = (0,0,255)
            else:
                posture = "Good"
                color = (0,255,0)

            h, w, _ = img.shape
            for lm in lms:
                cv2.circle(img, (int(lm.x*w), int(lm.y*h)), 3, color, -1)

        return img, posture
