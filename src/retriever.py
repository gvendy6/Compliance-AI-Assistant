# src/retriever.py

import numpy as np
from src.embeddings import embed_texts
from src.vector_store import load_faiss_index


def retrieve(query, k=5):
    index, chunks = load_faiss_index()

    query_embedding = embed_texts([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = [chunks[i] for i in indices[0]]
    return results