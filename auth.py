import streamlit as st
from database import register_user, login_user

def auth_page():
    st.markdown("## 🔐 PostureSense")

    choice = st.radio("", ["Login", "Register"], horizontal=True)

    if choice == "Register":
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")

        if st.button("Create Account"):
            res = register_user(name, phone, password)
            if res == "Success":
                st.success("Account created!")
            elif res == "Exists":
                st.error("Phone already exists")
            else:
                st.error("Invalid phone number")

    else:
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(phone, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.name = user[0]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")
