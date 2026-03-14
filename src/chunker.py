# src/chunker.py

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def load_documents(directory):
    documents = []

    print("\n🔍 Loading documents from:", directory)

    for file in os.listdir(directory):
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

                documents.append({
                    "text": text,
                    "source": file
                })

                print(f"   ✅ Loaded: {file} | Size: {len(text)} characters")

    print(f"\n📄 Total documents loaded: {len(documents)}\n")

    return documents


def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    all_chunks = []

    print("✂️ Creating chunks...\n")

    for doc in documents:
        chunks = splitter.split_text(doc["text"])

        print(f"   📘 {doc['source']} → {len(chunks)} chunks")

        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": doc["source"]
            })

    print(f"\n📦 Total chunks created: {len(all_chunks)}\n")

    return all_chunks