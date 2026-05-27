# AI Document Reader & Q&A Bot

A powerful AI-powered document reader that processes PDF files and answers questions about their content using semantic search and an LLM.

## Features

- 📄 **PDF Processing**: Upload and process PDF documents
- 🔍 **Vector Search**: Uses FAISS for fast semantic similarity search
- 🤖 **AI Q&A**: Ask questions about document content
- 📝 **Document Summarization**: Automatic document summaries
- 🌐 **Web Interface**: Streamlit-based user-friendly interface
- 💾 **Vector Storage**: Efficient FAISS-based vector database

## Prerequisites

- Python 3.8+
- Ollama installed and running (download from [ollama.com](https://ollama.com))
- Mistral model: `ollama pull mistral`

## Installation

1. **Navigate to the folder**:
   ```powershell
   cd "Document Reader & Q&A Bot"
   ```

2. **Create a virtual environment**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Ensure Ollama is running**:
   ```powershell
   ollama serve
   ```

## Running the Application

Start the Streamlit web interface:
```powershell
streamlit run ai_document_reader.py
```

The application will open in your default browser at `http://localhost:8501`

## How to Use

1. Upload a PDF file using the file uploader
2. The document will be processed and stored in the FAISS vector database
3. Ask questions about the document content
4. The AI will search the document and provide answers based on the content
5. Get automatic summaries of your documents

## Dependencies

- `langchain-ollama` - LangChain integration with Ollama
- `langchain-community` - Community components for LangChain
- `streamlit` - Web UI framework
- `faiss-cpu` - Vector similarity search
- `PyPDF2` - PDF processing
- `sentence-transformers` - Text embeddings
- `requests` - HTTP requests

## Technology Stack

- **LLM**: Ollama (Mistral model)
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector DB**: FAISS
- **UI Framework**: Streamlit
- **PDF Processing**: PyPDF2

## Troubleshooting

**Issue**: "ModuleNotFoundError"
- Solution: Ensure virtual environment is activated and all dependencies are installed

**Issue**: Ollama connection error
- Solution: Make sure Ollama is running with `ollama serve`

**Issue**: Out of memory
- Solution: Process smaller PDF files or reduce chunk size in the code

## Author

Created as part of the AIAgents project
