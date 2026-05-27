import requests
from bs4 import BeautifulSoup
import streamlit as st
import faiss
import numpy as np
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# Load AI Model
llm = Ollama(model="mistral")  # Change to "llama3" or another Ollama model

# Load Hugging Face Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384)  # Vector dimension for MiniLM
vector_store = {}  # Map FAISS index -> chunk text

# Function to scrape a website
def scrape_website(url):
    try:
        st.write(f"🌍 Scraping website: {url}")
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return f"⚠️ Failed to fetch {url}"
        
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text[:5000] if text else "⚠️ No text found"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to store data in FAISS
def store_in_faiss(text, url):
    global index, vector_store
    st.write("📥 Storing data in FAISS...")
    
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)

    vectors = embeddings.embed_documents(texts)
    vectors = np.array(vectors, dtype=np.float32)

    # Store each chunk individually
    start_id = index.ntotal
    index.add(vectors)
    for i, chunk in enumerate(texts):
        vector_store[start_id + i] = (url, chunk)

    return "✅ Data stored successfully!"

# Function to retrieve relevant chunks and answer questions
def retrieve_and_answer(query):
    global index, vector_store

    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)
    D, I = index.search(query_vector, k=3)  # Retrieve top 3 chunks

    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += vector_store[idx][1] + "\n\n"

    if not context:
        return "🤖 No relevant data found."

    return llm.invoke(f"Based on the following context, answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:")

# Streamlit Web UI
st.title("🤖 AI-Powered Web Scraper with FAISS Storage")
st.write("🔗 Enter a website URL below and store its knowledge for AI-based Q&A!")

url = st.text_input("🔗 Enter Website URL:")
if url:
    content = scrape_website(url)
    if "⚠️ Failed" in content or "❌ Error" in content:
        st.write(content)
    else:
        store_message = store_in_faiss(content, url)
        st.write(store_message)

query = st.text_input("❓ Ask a question based on stored content:")
if query:
    answer = retrieve_and_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)
