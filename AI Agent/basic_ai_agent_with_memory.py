#   Basic AI Agent with Memory
#   Has context memory using ChatMessageHistory, and a simple chat loop with the AI model.
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="deepseek-r1")

# Initialize Memory
chat_history = ChatMessageHistory()

# Define AI Chat Prompt
prompt = PromptTemplate(
    input_variables=["history", "question"],
    template="Previous conversation: {chat_history}\n\nUser: {question}\n\nAI:"
)

# Function to run AI Chat with Memory
def run_chain(question):
    # Retrieve chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])

    # Run the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user question and AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = run_chain(user_input)
    print(f"AI: {response}")

# Optional: Show full chat history at the end
print("\nChat History:")
for msg in chat_history.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")