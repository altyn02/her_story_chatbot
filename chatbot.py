import streamlit as st
import requests

st.title("Re:Her AI Chatbot")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

SYSTEM_PROMPT = """
You are Re:Her, a supportive chatbot helping migrant women in Korea.
Be warm, respectful and supportive.
Encourage reflection and conversation.
Keep responses simple and clear.
"""

def ask_llama(messages):

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["message"]["content"]


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello. What would you like to talk about today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Type your message")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        messages = [{"role":"system","content":SYSTEM_PROMPT}]
        messages += st.session_state.messages

        reply = ask_llama(messages)

        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
