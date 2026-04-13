import streamlit as st
import time
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from posture_core import PostureDetector

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.detector = PostureDetector()

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img, posture = self.detector.process(img)

        st.session_state.current_posture = posture

        return img

def home_page():
    st.title(f"👋 Welcome {st.session_state.name}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶ Start Session"):
            st.session_state.session_active = True

    with col2:
        if st.button("⏹ Stop Session"):
            st.session_state.session_active = False

    webrtc_streamer(key="posture", video_transformer_factory=VideoProcessor)

    posture = st.session_state.get("current_posture", "Waiting")

    st.subheader(f"Posture: {posture}")

    # 🔴 Red screen
    if posture == "Bad" and st.session_state.get("session_active"):
        st.markdown(
            "<div style='position:fixed;top:0;left:0;width:100%;height:100%;background:red;opacity:0.2;z-index:999'></div>",
            unsafe_allow_html=True
        )

    # 🔊 Voice Alert
    if posture == "Bad":
        st.markdown("""
        <script>
        var msg = new SpeechSynthesisUtterance("Fix your posture");
        window.speechSynthesis.speak(msg);
        </script>
        """, unsafe_allow_html=True)
