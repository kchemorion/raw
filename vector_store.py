# vector_store.py

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from initialize_embeddings import create_embeddings

# Define a function to create a vector store
def create_vector_store(documents):
    text_splitter = CharacterTextSplitter(chunk_size=400, separator=" ")
    docs = [split for doc in documents for split in text_splitter.split_text(doc)]
    embeddings = [create_embeddings(doc) for doc in docs]
    metadatas = [{"source": doc} for doc in docs]  # corrected to align with docs
    store = FAISS.from_texts(docs, embeddings, metadatas=metadatas)
    return store

if __name__ == "__main__":
    # Example documents
    documents = ["Sample text document for testing."]
    store = create_vector_store(documents)
    store.save_local('./vector_store')
