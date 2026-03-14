# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===== Chunk Settings =====
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ===== Embedding Model =====
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ===== LLM Model (Ollama) =====
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "models/gemini-2.5-flash"   # or gemini-1.5-pro

# ===== Vector DB =====
VECTOR_DB_PATH = "vector_store.index"
CHUNKS_FILE_PATH = "chunks.pkl"

# ===== Data Path =====
DATA_PATH = "data/processed"