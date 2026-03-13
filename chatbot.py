import os
import streamlit as st
from openai import OpenAI

st.title("Re:Her AI Chatbot")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY is not set. Please add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

user_input = st.text_input("Ask something")

if user_input:
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )
        st.write(response.output_text)
    except Exception as e:
        st.error(f"Error: {e}")
