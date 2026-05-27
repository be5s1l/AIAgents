# Personal AI Assistant - Voice Assistant

A voice-based AI assistant that listens to user queries, processes them through a local LLM, and responds with spoken answers while maintaining conversation history.

## Features

- 🎤 **Voice Recognition**: Accepts voice input from microphone
- 🤖 **AI Processing**: Uses local Ollama LLM for offline processing (no API keys needed)
- 💾 **Memory**: Maintains chat history for context-aware responses
- 🔊 **Text-to-Speech**: Provides spoken responses
- ⌨️ **Fallback Input**: Keyboard input when microphone is unavailable
- 🌐 **Web UI Option**: Streamlit-based web interface available

## Available Versions

### 1. Voice Assistant (`ai_voice_assistant.py`)
Command-line voice assistant with conversation memory and text-to-speech output.

### 2. Voice Assistant with UI (`ai_voice_assistant_ui.py`)
Web-based Streamlit interface for the voice assistant with enhanced UI.

## Prerequisites

- Python 3.8+
- Ollama installed and running (download from [ollama.ai](https://ollama.ai))
- Microphone (optional - keyboard input available as fallback)
- Mistral model: `ollama pull mistral`

Alternative models:
- `ollama pull deepseek-r1` (advanced reasoning)
- `ollama pull llama2` (lightweight)
- `ollama pull neural-chat` (optimized for conversation)

## Installation

1. **Navigate to the folder**:
   ```powershell
   cd "Personal AI Assistant"
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
   - Download and install from [ollama.ai](https://ollama.ai)
   - Verify installation: `ollama --version`

5. **Start Ollama server** (in a separate terminal):
   ```powershell
   ollama serve
   ```

6. **Pull a language model**:
   ```powershell
   ollama pull mistral
   ```

## Running the Application

### Command-line Version:
```powershell
python ai_voice_assistant.py
```

### Web UI Version:
```powershell
streamlit run ai_voice_assistant_ui.py
```

## How to Use

1. **Start the assistant**: Run one of the versions above
2. **Listen for prompts**: The assistant will prompt you to speak or type
3. **Provide input**: 
   - Speak into your microphone when prompted with "🎤 Listening..."
   - Or type your question if microphone is unavailable
4. **Receive response**: The assistant will respond with audio and text
5. **Exit**: Type "exit" or "stop" to quit the assistant

## Features Explained

### Voice Recognition
- Uses `speech_recognition` library to capture microphone input
- Automatically detects speech and converts to text
- Fallback to keyboard input if microphone fails

### AI Processing
- Uses Ollama running locally for complete offline processing
- No internet connection required after model download
- Support for various Mistral, LLaMA, and other models

### Text-to-Speech
- Uses `pyttsx3` for speaking responses
- Cross-platform support (Windows, Mac, Linux)
- Natural-sounding voice output

### Conversation Memory
- Maintains chat history throughout the session
- Context-aware responses using conversation history
- Displays full conversation summary on exit

## Dependencies

- `langchain-ollama==0.2.1` - LangChain integration with Ollama
- `langchain-core==0.3.28` - Core LangChain components
- `langchain-community==0.3.12` - Community components
- `ollama==0.3.10` - Ollama Python client
- `speech-recognition==3.10.1` - Voice recognition
- `pyttsx3==2.90` - Text-to-speech
- `streamlit` - Web UI (for UI version)
- `pyaudio==0.2.14` - Audio processing

## Technology Stack

- **LLM**: Ollama (Mistral, LLaMA, or other models)
- **Voice Input**: SpeechRecognition library
- **Audio Output**: pyttsx3 (offline TTS)
- **Framework**: LangChain
- **UI**: Streamlit (for web version)

## Troubleshooting

### ModuleNotFoundError
- Solution: Ensure you've activated the virtual environment and installed requirements
  ```powershell
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

### Microphone not detected
- Solution: Check your system audio settings
- Fallback: Use keyboard input when prompted
- Alternative: Run the UI version

### Ollama connection error
- Solution: Make sure Ollama is running in another terminal with `ollama serve`
- Check that Ollama is listening on `localhost:11434`

### No audio output
- Solution: Check system volume settings
- Verify pyttsx3 is properly installed
- Try adjusting the speaking rate in the code

### Model not found
- Solution: Pull the model first
  ```powershell
  ollama pull mistral
  ```

## Performance Tips

- Use `mistral` model for balanced performance
- Use `neural-chat` for faster responses
- Use `deepseek-r1` for more advanced reasoning
- First response may take longer as the model initializes

## Notes

- Ensure Ollama is running before starting the assistant
- Internet connection required for initial model download
- No API keys needed - completely local and private
- Conversation history is maintained during the session

## Author

Created as part of the AIAgents project
