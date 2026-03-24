# Basic AI Agent Project

This project contains three versions of a basic AI agent using LangChain and Ollama.

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running (download from https://ollama.com/)
- The "deepseek-r1" model pulled in Ollama: `ollama pull deepseek-r1`

## Installation

1. Clone or download this repository.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`

## Versions

### 1. Basic AI Agent (`basic_ai_agent.py`)

A simple command-line AI chatbot without memory.

**How to run:**
```bash
python basic_ai_agent.py
```

Type your questions and press Enter. Type 'exit' or 'quit' to stop.

### 2. Basic AI Agent with Memory (`basic_ai_agent_with_memory.py`)

A command-line AI chatbot with conversation memory.

**How to run:**
```bash
python basic_ai_agent_with_memory.py
```

The AI remembers the conversation history. Type 'exit' or 'quit' to stop and see the full chat history.

### 3. Basic AI Agent with Web UI (`basic_ai_agent_with_webUI.py`)

A web-based AI chatbot with memory using Streamlit.

**How to run:**
```bash
streamlit run basic_ai_agent_with_webUI.py
```

Open the provided URL in your browser to chat with the AI. The chat history is displayed below.

## Notes

- Ensure Ollama is running before executing any of the scripts.
- The AI model used is "deepseek-r1". You can change it in the code if needed.