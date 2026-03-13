import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Re:Her AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )
    st.write(response.output_text)
