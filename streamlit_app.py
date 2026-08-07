import streamlit as st
from app.chains.career_chain import career_chain
from pathlib import Path
import tempfile
from app.rag.loaders import load_document
from app.rag.splitter import split_documents


st.title("🚀 LangChain Career Coach")

question = st.text_area("Ask a career-related question")

if st.button("Ask"):
    response = career_chain.invoke(
        {
            "question": question
        }
    )

    st.write(response)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    suffix = Path(uploaded_file.name).suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        file_path = tmp_file.name

    documents = load_document(file_path)

    chunks = split_documents(documents)

    st.success(f"Loaded {len(documents)} document(s)")
    st.info(f"Created {len(chunks)} chunks")