# src/vector_store.py

import faiss
import numpy as np
import pickle
from src.config import VECTOR_DB_PATH, CHUNKS_FILE_PATH


def create_faiss_index(embeddings, chunks):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, VECTOR_DB_PATH)

    with open(CHUNKS_FILE_PATH, "wb") as f:
        pickle.dump(chunks, f)


def load_faiss_index():
    index = faiss.read_index(VECTOR_DB_PATH)

    with open(CHUNKS_FILE_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks