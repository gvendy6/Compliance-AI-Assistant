# src/ingest.py

from src.chunker import load_documents, create_chunks
from src.embeddings import embed_texts
from src.vector_store import create_faiss_index
from src.config import DATA_PATH


def run_ingestion():
    print("Loading documents...")
    docs = load_documents(DATA_PATH)

    print("Applying recursive chunking...")
    chunks = create_chunks(docs)

    texts = [c["text"] for c in chunks]

    print("Generating embeddings...")
    embeddings = embed_texts(texts)

    print("Creating FAISS index...")
    create_faiss_index(embeddings, chunks)

    print("Ingestion complete!")


if __name__ == "__main__":
    run_ingestion()