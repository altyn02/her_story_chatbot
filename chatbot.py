import requests
import streamlit as st

st.set_page_config(page_title="Re:Her Chatbot", page_icon="💬", layout="centered")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2"

SYSTEM_PROMPT = """
You are Re:Her, a supportive AI chatbot for migrant and marriage migrant women living in South Korea.

Your goals:
- provide a safe space for reflection
- offer gentle guidance
- be culturally sensitive
- support multilingual conversations
- help users organize thoughts and feelings

Your style:
- warm, calm, respectful
- clear and simple
- not judgmental
- if the user writes in Russian, Korean, or English, reply in that language when possible

Important boundaries:
- do not claim to be a therapist, doctor, or lawyer
- do not provide professional medical or legal advice
- encourage seeking local help in emergencies
""".strip()


def ask_ollama(messages):
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]


st.title("Re:Her AI Chatbot")
st.caption("Free local prototype using Streamlit + Ollama + Llama")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Welcome. This is a quiet and supportive space. What would you like to talk about today?",
        }
    ]

with st.sidebar:
    st.header("Settings")

    if st.button("Clear conversation"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Welcome. This is a quiet and supportive space. What would you like to talk about today?",
            }
        ]
        st.rerun()

    starter = st.selectbox(
        "Starter topic",
        [
            "None",
            "I feel lonely in Korea.",
            "I struggle with the language barrier.",
            "I want to feel more confident at work.",
            "Помоги мне выразить мои мысли.",
        ],
    )

    if st.button("Use starter topic") and starter != "None":
        st.session_state.messages.append({"role": "user", "content": starter})
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                ollama_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                ollama_messages.extend(st.session_state.messages)

                reply = ask_ollama(ollama_messages)
            except requests.exceptions.ConnectionError:
                reply = (
                    "I can't connect to Ollama. Please make sure Ollama is installed and running, "
                    "and that the llama3.2 model has been pulled."
                )
            except Exception as e:
                reply = f"Something went wrong: {e}"

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

st.divider()
st.markdown(
    "**Note:** This is a prototype for guidance and reflection. "
    "It is not a substitute for professional medical, legal, or mental health support."
)
