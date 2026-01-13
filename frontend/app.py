import streamlit as st
import requests

BACKEND_URL = "http://backend:8000/message"

st.title("Frontend")

if st.button("Fetch message"):
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
        st.success(data["message"])
        st.write("Time:", data["time"])
    except Exception:
        st.error("Backend not reachable")
