#   Basic AI Agent
#   Has no context memory, just a simple chat loop with the AI model.
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="deepseek-r1")

# Simple chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = llm.invoke(user_input)
    print(f"AI: {response}")
    
    