import streamlit as st
import ollama
import json

st.set_page_config(page_title="Nectar AI Chatbot", layout="wide")

st.title("🤖 Nectar`s AI Chatbot")

# Sidebar controls
st.sidebar.header("⚙️ Settings")

model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["phi"],
    index=0
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Export chat button
if st.sidebar.button("💾 Export Chat"):
    if "messages" in st.session_state and st.session_state.messages:
        chat_json = json.dumps(st.session_state.messages, indent=2)
        st.sidebar.download_button(
            label="Download Chat",
            data=chat_json,
            file_name="chat_history.json",
            mime="application/json"
        )

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        response = ollama.chat(
            model=model_choice,
            messages=st.session_state.messages
        )

        ai_reply = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )

    with st.chat_message("assistant"):
        st.write(ai_reply)
