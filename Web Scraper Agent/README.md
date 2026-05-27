# AI-Powered Web Scraper

An intelligent web scraper that extracts content from websites and automatically summarizes it using AI.

## Features

- 🌍 **Website Scraping**: Extract content from any website
- 🤖 **AI Summarization**: Summarize content using local LLM
- 🎯 **Smart Parsing**: Extracts text content intelligently using BeautifulSoup
- 🌐 **Web Interface**: Easy-to-use Streamlit UI
- ⚡ **Fast Processing**: Real-time content extraction and analysis
- 📊 **Multiple Versions**: Two implementations available

## Available Versions

### 1. Basic Web Scraper (`ai_web_scraper.py`)
Simple web scraper with AI summarization using Streamlit.

### 2. Web Scraper with FAISS (`ai_web_scraper_fiass.py`)
Advanced version with FAISS vector database for semantic search and retrieval.

## Prerequisites

- Python 3.8+
- Ollama installed and running (download from [ollama.com](https://ollama.com))
- Mistral model: `ollama pull mistral`

## Installation

1. **Navigate to the folder**:
   ```powershell
   cd "Web Scraper Agent"
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
# For basic web scraper
streamlit run ai_web_scraper.py

# For advanced version with FAISS
streamlit run ai_web_scraper_fiass.py
```

The application will open in your default browser at `http://localhost:8501`

## How to Use

1. Enter a website URL in the text input field
2. The scraper will fetch and extract content from the website
3. The AI will automatically summarize the extracted content
4. View the summary in the web interface

## Features Explained

- **URL Input**: Enter any website URL
- **Content Extraction**: Automatically extracts paragraph text from HTML
- **AI Summarization**: Uses Mistral LLM to create concise summaries
- **Error Handling**: Gracefully handles network errors and invalid URLs
- **User Agent**: Includes proper headers to avoid blocking

## Dependencies

- `streamlit` - Web UI framework
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing
- `langchain-ollama` - LangChain integration with Ollama
- `langchain-community` - Community components for LangChain
- `faiss-cpu` - Vector similarity search (for FAISS version)
- `sentence-transformers` - Text embeddings (for FAISS version)

## Technology Stack

- **LLM**: Ollama (Mistral model)
- **Web Scraping**: BeautifulSoup4 + Requests
- **Vector DB**: FAISS (advanced version)
- **UI Framework**: Streamlit

## Troubleshooting

**Issue**: "Failed to fetch [URL]"
- Solution: Check your internet connection and ensure the URL is valid

**Issue**: "No text found"
- Solution: The website may have JavaScript-rendered content that BeautifulSoup cannot extract

**Issue**: Connection timeout
- Solution: Try a different website or increase the timeout value in the code

**Issue**: ModuleNotFoundError
- Solution: Ensure virtual environment is activated and all dependencies are installed

## Notes

- The scraper respects website structure and extracts paragraph content
- Summaries are limited to first 1000 characters of extracted content
- Include proper User-Agent headers to avoid being blocked
- Some websites may have robots.txt restrictions

## Author

Created as part of the AIAgents project
