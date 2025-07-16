# Clone the repo

# Create and activate virtual environment
python -m venv venv && \
source venv/bin/activate && \

# Install dependencies
pip install -r requirements.txt && \

# Pull Ollama model (if not already available)
ollama pull llama3 && \

# Start Ollama in the background (optional if already running)
# ollama serve &

# Fill ChromaDB vector store
python fill_db.py && \

# Ask your RAG question using Ollama
python ask.py
