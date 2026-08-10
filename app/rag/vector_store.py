from uuid import uuid4

from langchain_chroma import Chroma
from app.rag.embeddings import embeddings


def create_vector_store(chunks):

    collection_name = f"resume_{uuid4().hex}"

    # print("CREATING NEW VECTOR STORE:", collection_name)
    # print("FIRST CHUNK:")
    # print(chunks[0].page_content[:500])

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=collection_name
    )

    return vector_store