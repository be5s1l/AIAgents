# AI Agents Project

This project contains AI agent implementations for various tasks including voice assistants and web-based agents.

## Project Structure

```
AIAgents/
├── AI Agent/
│   ├── basic_ai_agent.py
│   ├── basic_ai_agent_with_memory.py
│   ├── basic_ai_agent_with_webUI.py
│   └── requirements.txt
├── Personal AI Assistant/
│   └── ai_voice_assistant.py
└── requirements.txt
```

## Personal AI Assistant - Voice Assistant

A voice-based AI assistant that listens to user queries, processes them through a local LLM, and responds with spoken answers while maintaining conversation history.

### Features

- 🎤 **Voice Recognition**: Accepts voice input from microphone
- 🤖 **AI Processing**: Uses local Ollama LLM for offline processing (no API keys needed)
- 💾 **Memory**: Maintains chat history for context-aware responses
- 🔊 **Text-to-Speech**: Provides spoken responses
- ⌨️ **Fallback Input**: Keyboard input when microphone is unavailable

### Prerequisites

1. **Python 3.8+**
2. **Ollama** - Download from [ollama.ai](https://ollama.ai)
3. **Microphone** (optional - keyboard input available as fallback)

### Installation

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

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Install Ollama**:
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - After installation, verify Ollama is working by running in a terminal:
     ```powershell
     ollama --version
     ```

5. **Pull the Mistral model**:
   ```powershell
   ollama pull mistral
   ```
   
   Alternative models available:
   - `ollama pull deepseek-r1` (more advanced reasoning)
   - `ollama pull llama2` (lighter weight)
   - `ollama pull neural-chat` (optimized for conversation)

### Running the Voice Assistant

1. **Start Ollama** (in a separate terminal):
   ```powershell
   ollama serve
   ```
   This starts the LLM server on `localhost:11434`

2. **Run the assistant** (in another terminal):
   ```powershell
   cd "Personal AI Assistant"
   python ai_voice_assistant.py
   ```

3. **Interact with the assistant**:
   - The assistant will greet you
   - Speak into your microphone when prompted with "🎤 Listening..."
   - The assistant will process your query and respond
   - Type "exit" or "stop" to quit the assistant

### Troubleshooting

**Error: `ModuleNotFoundError: No module named 'speech_recognition'`**
- Solution: Ensure you've activated the virtual environment and installed requirements:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

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
