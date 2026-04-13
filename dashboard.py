import streamlit as st

def dashboard_page():
    st.title("📊 Posture Dashboard")

    st.write("Your posture analytics will appear here")

    st.info("💡 Tips:")
    tips = [
        "Sit straight",
        "Keep screen at eye level",
        "Take breaks",
        "Keep shoulders relaxed"
    ]

    for t in tips:
        st.write("✔", t)
