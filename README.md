# 🤖 AI Agents Project

A comprehensive collection of AI-powered agents built with LangChain and Ollama. All agents run locally without requiring API keys - completely private and offline after model download.

## 📋 Project Overview

This repository contains multiple intelligent agents for different tasks:

| Agent | Description | Type | Status |
|-------|-------------|------|--------|
| **Basic AI Agent** | Chatbot with command-line interface | CLI | ✅ Ready |
| **AI Agent with Memory** | Chatbot with conversation history | CLI | ✅ Ready |
| **AI Agent with Web UI** | Chatbot with Streamlit web interface | Web | ✅ Ready |
| **Voice Assistant** | AI assistant with speech recognition & TTS | CLI | ✅ Ready |
| **Voice Assistant UI** | Voice assistant with web interface | Web | ✅ Ready |
| **Document Reader Q&A** | PDF processor with semantic search | Web | ✅ Ready |
| **Web Scraper** | Website content extraction & summarization | Web | ✅ Ready |

## 📁 Project Structure

```
AIAgents/
├── AI Agent/                          # Basic chatbot implementations
│   ├── basic_ai_agent.py             # Simple CLI chatbot
│   ├── basic_ai_agent_with_memory.py # CLI with conversation memory
│   ├── basic_ai_agent_with_webUI.py  # Web UI with Streamlit
│   └── requirements.txt
├── Personal AI Assistant/             # Voice-based assistant
│   ├── ai_voice_assistant.py         # CLI voice assistant
│   ├── ai_voice_assistant_ui.py      # Web UI voice assistant
│   └── requirements.txt
├── Document Reader & Q&A Bot/         # PDF processing
│   ├── ai_document_reader.py         # PDF Q&A system
│   └── requirements.txt
├── Web Scraper Agent/                 # Web content extraction
│   ├── ai_web_scraper.py             # Basic scraper
│   ├── ai_web_scraper_fiass.py       # Advanced with FAISS
│   └── requirements.txt
├── README.md                          # This file
├── requirements.txt                   # Root dependencies
└── .gitignore                         # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed - Download from [ollama.com](https://ollama.com)
3. Microphone (optional for voice features)

### Global Installation

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/be5s1l/AIAgents.git
   cd AIAgents
   ```

2. **Create a virtual environment**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install global dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Start Ollama server** (keep this running):
   ```powershell
   ollama serve
   ```

5. **Pull a language model**:
   ```powershell
   ollama pull mistral
   ```

### Project-Specific Usage

Each project folder contains its own README with detailed instructions. Navigate to any project folder and run:

```powershell
# Install project-specific dependencies
pip install -r requirements.txt

# Run the specific agent
python script_name.py
# or for Streamlit apps
streamlit run script_name.py
```

## 🎯 Projects Overview

### [AI Agent](AI%20Agent/README.md)
Three versions of a basic chatbot using LangChain and Ollama:
- **Basic**: Simple Q&A without memory
- **With Memory**: Maintains conversation history
- **With Web UI**: Streamlit interface for easy interaction

**Quick Start**: `cd "AI Agent" && streamlit run basic_ai_agent_with_webUI.py`

### [Personal AI Assistant](Personal%20AI%20Assistant/README.md)
Voice-enabled AI assistant with offline speech recognition:
- 🎤 Voice input (with keyboard fallback)
- 🔊 Spoken responses via text-to-speech
- 💾 Conversation memory
- 🌐 Web UI option available

**Quick Start**: `cd "Personal AI Assistant" && python ai_voice_assistant.py`

### [Document Reader & Q&A Bot](Document%20Reader%20%26%20Q&A%20Bot/README.md)
Intelligent PDF processor with semantic search:
- 📄 Upload and process PDF files
- 🔍 FAISS-based vector search
- 🤖 AI-powered question answering
- 📝 Automatic document summarization

**Quick Start**: `cd "Document Reader & Q&A Bot" && streamlit run ai_document_reader.py`

### [Web Scraper Agent](Web%20Scraper%20Agent/README.md)
Extract and summarize website content:
- 🌍 Scrape any website
- 🤖 AI-powered summarization
- ⚡ Two versions (basic & advanced with FAISS)
- 🌐 Web UI for easy use

**Quick Start**: `cd "Web Scraper Agent" && streamlit run ai_web_scraper.py`

## 💾 System Requirements

| Component | Requirement |
|-----------|-------------|
| Python | 3.8 or higher |
| RAM | 4GB minimum (8GB+ recommended) |
| Disk Space | 5GB+ (for models) |
| Internet | Required for initial setup; offline after model download |

## 🧠 Available Language Models

All projects use Ollama with support for:

- **mistral** (recommended) - Fast, balanced performance
- **llama2** - Lightweight, good for constrained systems
- **neural-chat** - Optimized for conversation
- **deepseek-r1** - Advanced reasoning capabilities
- **openchat** - Fast inference
- And many more...

Pull any model with: `ollama pull model_name`

## 📋 Dependencies

Each project has specific requirements in its `requirements.txt`. Common libraries include:

- **langchain-ollama** - LLM integration
- **langchain-community** - Community tools
- **streamlit** - Web interfaces
- **faiss-cpu** - Vector similarity search
- **speech-recognition** - Voice input
- **pyttsx3** - Text-to-speech
- **beautifulsoup4** - Web scraping

## 🔧 Troubleshooting

### Common Issues

**Ollama connection error**
```powershell
# Make sure Ollama is running
ollama serve
```

**Module not found errors**
```powershell
# Activate virtual environment and reinstall
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Microphone not working**
- Check system audio settings
- Use keyboard input fallback
- Try running the Streamlit UI version

**Out of memory**
- Use a lighter model: `ollama pull llama2`
- Reduce batch size in code
- Close other applications

### For Detailed Help

Check the individual README in each project folder for specific troubleshooting.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add new agents

## 📄 License

This project is open source and available under the MIT License.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🌟 Features Highlights

✅ **Completely Offline** - No API keys, no data sent to external services  
✅ **Local Processing** - All computation happens on your machine  
✅ **Multiple Interfaces** - CLI and Web UI options  
✅ **Modular Design** - Mix and match components  
✅ **Easy Setup** - Simple installation with clear instructions  
✅ **Well Documented** - Each project has detailed documentation  
✅ **Active Maintenance** - Regular updates and improvements  

## 🚀 Next Steps

1. Choose an agent from the list above
2. Navigate to its folder
3. Follow the installation steps in its README
4. Start experimenting!

Happy coding! 🎉

**Error: `[WinError 10061] No connection could be made`**
- Solution: Ollama server is not running. Start it in a separate terminal:
  ```powershell
  ollama serve
  ```

**Error: `⚠️ Microphone input is not available`**
- The system will automatically fall back to keyboard input. Simply type your query instead.

**No speech recognition on Linux/Mac**
- Some systems require additional audio libraries. Install:
  - **Ubuntu/Debian**: `sudo apt-get install portaudio19-dev`
  - **MacOS**: `brew install portaudio`

### Configuration

You can modify the following settings in `ai_voice_assistant.py`:

```python
llm = OllamaLLM(model="mistral")  # Change the model
engine.setProperty("rate", 160)   # Adjust speaking speed (words per minute)
```

### Changing the LLM Model

To use a different model, modify line 8 in `ai_voice_assistant.py`:

```python
# Current
llm = OllamaLLM(model="mistral")

# Alternative examples
llm = OllamaLLM(model="deepseek-r1")
llm = OllamaLLM(model="llama2")
llm = OllamaLLM(model="neural-chat")
```

Then pull the model first:
```powershell
ollama pull <model_name>
```

### System Requirements

- **RAM**: Minimum 4GB (recommended 8GB+)
- **Disk Space**: 5GB+ for LLM models
- **CPU**: Multi-core recommended
- **Network**: Internet required for initial model download only

### Dependencies

See `requirements.txt` for complete list of dependencies:
- `speech_recognition` - Voice input processing
- `pyttsx3` - Text-to-speech engine
- `langchain-ollama` - LLM integration
- `langchain-core` - Core LangChain utilities
- `langchain-community` - Community integrations
- `ollama` - Ollama Python client

### License

This project is open source. Check the LICENSE file for details.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
