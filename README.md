# 🧠 Build a RAG System with Python, ChromaDB & Ollama
> ⚡ No API keys needed. Everything runs locally.

## ✅ Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com/download) (install & ensure `ollama serve` is running)
- Git

---

## 🚀 Quick Setup

To clone, install, run embedding, and query RAG — just run the following one-liner:

```bash
git clone https://github.com/ThomasJanssen-tech/Retrieval-Augmented-Generation.git && \
cd Retrieval-Augmented-Generation && \
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
ollama pull llama3 && \
python fill_db.py && \
python ask.py
