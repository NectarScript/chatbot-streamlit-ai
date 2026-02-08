<<<<<<< HEAD
# chatbot-streamlit-ai
AI chatbot built with Streamlit and Ollama for local LLM interaction.
=======
# 🤖 AI Chatbot (Local LLM)

An interactive AI chatbot built using **Streamlit** and a locally hosted language model via **Ollama**.
The application supports conversational memory and runs completely offline without relying on paid cloud APIs.

---

## 🚀 Features

* Real-time conversational chatbot
* Chat memory using session state
* Clean chat-style UI
* Local LLM integration (offline)
* No API keys or cloud dependency
* Exportable and reproducible project setup

---

## 🛠 Tech Stack

* Python
* Streamlit
* Ollama (Phi model)

---

## 📂 Project Structure

```
chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Install Ollama

Download and install Ollama from:

[https://ollama.com](https://ollama.com)

### 3. Pull the model

```
ollama pull phi
```

### 4. Run the application

```
streamlit run app.py
```

The chatbot will open in your browser.

---

## 💡 How It Works

The chatbot sends user messages to a locally running language model through Ollama.
Conversation history is stored using Streamlit session state to maintain chat memory.

---

## 📈 Future Improvements

* Response streaming
* Multiple model support
* Conversation export
* UI theming
* Voice input/output

---

## 📄 License

This project is for educational and portfolio purposes.
>>>>>>> a5980f9 (Initial chatbot release)
