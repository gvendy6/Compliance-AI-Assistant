#ui.py
import streamlit as st
from src.agent import ask_agent

st.set_page_config(page_title="Compliance AI", layout="wide")

st.title("🏦 Compliance AI Assistant")
st.markdown("Ask questions about your policy documents.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask a compliance question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("Analyzing policy documents..."):
        response = ask_agent(user_input)

    st.session_state.chat_history.append(("assistant", response))

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)