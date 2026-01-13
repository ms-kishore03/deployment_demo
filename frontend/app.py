import streamlit as st
import requests

BACKEND_URL = "https://deployment-demo-backend-dqif.onrender.com/message"

st.title("Frontend")

if st.button("Fetch message"):
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
        st.success(data["message"])
        st.write("Time:", data["time"])
    except Exception:
        st.error("Backend not reachable")
