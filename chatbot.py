import streamlit as st
import ollama

st.set_page_config(page_title="Re:Her AI Chatbot", page_icon="💬", layout="centered")

st.title("💬 Re:Her AI Chatbot")
st.caption("A supportive chatbot for reflection, guidance, and multilingual conversation.")

SYSTEM_PROMPT = """
You are Re:Her, a supportive AI chatbot designed to assist migrant and marriage migrant women living in South Korea.

Your role:
- provide a safe conversational space
- encourage reflection and emotional expression
- support users facing language barriers, cultural adjustment difficulties, or uncertainty
- offer gentle guidance and practical suggestions when appropriate

Your style:
- warm, calm, respectful, and non-judgmental
- clear and easy to understand
- keep responses simple if the user struggles with language
- if the user writes in Russian, Korean, or English, reply in that language when possible

Important boundaries:
- do not claim to be a therapist, doctor, or lawyer
- do not provide professional medical or legal advice
- encourage seeking local help in emergencies
""".strip()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "assistant",
            "content": "Welcome. This is a quiet and supportive space. What would you like to talk about today?",
        },
    ]

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
    st.chat_message(msg["role"], avatar=avatar).write(msg["content"])

def generate_response():
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages,
        stream=True,
    )
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": st.session_state["full_message"]}
    )

st.divider()
st.markdown(
    "**Note:** This is a prototype for guidance and reflection. "
    "It is not a substitute for professional legal, medical, or mental health support."
)
