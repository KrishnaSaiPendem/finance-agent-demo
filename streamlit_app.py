import streamlit as st
import requests

st.title("Autonomous Finance Agent")

user = st.text_input("User ID", "u1")
query = st.text_input("Ask about your spending…", "dining")

if st.button("Ask"):
    res = requests.get(
        "http://localhost:8001/query",
        params={"user_id": user, "q": query}
    ).json()
    st.markdown(f"**Agent:** {res['answer']}")
