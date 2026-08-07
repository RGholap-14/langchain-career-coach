from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)


def load_document(file_path: str):
    """
    Load a PDF or DOCX document and return LangChain Documents.
    """
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")

    return loader.load()