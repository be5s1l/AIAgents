#   Basic AI Agent with Web UI
#   Has context memory using ChatMessageHistory,and a simple Streamlit interface 
#   for chatting with the AI model.
import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="deepseek-r1")

# Initialize Memory
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()  # Stores user-AI conversation history

# Define AI Chat Prompt
prompt = PromptTemplate(
    input_variables=["history", "question"],
    template="Previous conversation: {chat_history}\n\nUser: {question}\n\nAI:"
)

# Function to run AI Chat with Memory
def run_chain(question):
    # Retrieve chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    # Run the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user question and AI response in memory
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

# Streamlit UI
st.title("AI Chatbot with Memory")
st.write("Ask me anything!")

user_input = st.text_input("Your Question:")
if user_input:
    response = run_chain(user_input)
    st.write(f"You: {user_input}")
    st.write(f"AI: {response}")

# Show full chat history
st.subheader("Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"{msg.type.capitalize()}: {msg.content}")