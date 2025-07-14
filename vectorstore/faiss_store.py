
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

FAISS_DB_PATH="faiss_index"

# ✅ Old (working) embedding import
embedding_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def create_vector_store(texts:list[str],metadatas:list[dict]=None):
    documents = [Document(page_content=txt,metadata=meta or {}) for txt, meta in zip(texts, metadatas or [{}] * len(texts))]
    return FAISS.from_documents(documents,embedding_model)


def save_vector_store(db):
    db.save_local(FAISS_DB_PATH)


def load_vector_store():
    if not os.path.exists(FAISS_DB_PATH):
        return None
    return FAISS.load_local(
        FAISS_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True  # required to load .pkl safely
    )


def add_to_vector_store(text:str,metadata:dict=None):
    db=load_vector_store()
    if db is None:
        db=create_vector_store([text], [metadata])
    else:
        new_db=create_vector_store([text], [metadata])
        db.merge_from(new_db)
    save_vector_store(db)


def search_vector_store(query:str,k:int=3):
    db=load_vector_store()
    if db is None:
        return []
    return db.similarity_search(query,k=k)

