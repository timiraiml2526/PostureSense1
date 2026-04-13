import streamlit as st
from auth import auth_page
from home import home_page
from dashboard import dashboard_page

st.set_page_config(page_title="PostureSense", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if not st.session_state.logged_in:
    auth_page()
    st.stop()

# Navigation
page = st.sidebar.radio("Navigation", ["Home", "Dashboard"])

if page == "Home":
    home_page()
else:
    dashboard_page()
