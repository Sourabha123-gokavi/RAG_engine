import chromadb
from dotenv import load_dotenv
from ollama import Client

# Load environment variables from .env (if needed)
load_dotenv()

# === Settings ===
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

# === Connect to Chroma vector DB ===
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="growing_vegetables")

# === Take user query ===
user_query = input("What do you want to know about growing vegetables?\n\n")

# === Retrieve top 4 similar chunks ===
results = collection.query(
    query_texts=[user_query],
    n_results=4
)

# Print matched documents (for debugging)
print("\n🔎 Retrieved Documents:\n")
for doc in results['documents'][0]:
    print(f"• {doc}\n")

# === Build prompt with retrieved context ===
context = "\n\n".join(results['documents'][0])

system_prompt = f"""
You are a helpful assistant. You answer questions about growing vegetables in Florida. 
Only use the information I am giving you. Do NOT use your own knowledge. 
If the answer is not in the data, just say: "I don't know".

--------------------How
The data:
{context}

User question: {user_query}
"""

# === Use Ollama's local model ===
client = Client(host='http://localhost:11434')

response = client.chat(
    model='llama3',  # make sure it's installed via `ollama run llama3`
    messages=[
        {"role": "user", "content": system_prompt}
    ]
)

# === Display the result ===
print("\n\n---------------------\n\n")
print("🧠 Answer:")
print(response['message']['content'])
