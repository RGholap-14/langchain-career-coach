import streamlit as st
from pathlib import Path
import tempfile

from app.chains.career_chain import career_chain
from app.rag.loaders import load_document
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_retriever
from app.chains.rag_chain import create_rag_chain
from app.chains.job_match_chain import create_job_match_chain


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LangChain Career Coach",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 LangChain Career Coach")


# ============================================================
# GENERAL CAREER CHAT
# ============================================================

st.header("💼 Career Coach")

career_question = st.text_area(
    "Ask a career-related question",
    placeholder="Example: How can I prepare for a Python interview?"
)

if st.button("Ask", key="career_button"):

    if career_question:

        response = career_chain.invoke(
            {
                "question": career_question
            }
        )

        st.write(response)

    else:
        st.warning("Please enter a question.")


st.divider()


# ============================================================
# RESUME UPLOAD
# ============================================================

st.header("📄 Resume Assistant")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"],
    key="resume_uploader"
)


if uploaded_file:

    # --------------------------------------------------------
    # Process uploaded resume
    # --------------------------------------------------------

    suffix = Path(uploaded_file.name).suffix

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as tmp_file:

        tmp_file.write(uploaded_file.getbuffer())
        file_path = tmp_file.name


    # Load document
    documents = load_document(file_path)

    # Split document
    chunks = split_documents(documents)

    # Create a fresh ChromaDB vector store
    vector_store = create_vector_store(chunks)

    # Create retriever
    retriever = get_retriever(vector_store)

    # Create RAG chain
    rag_chain = create_rag_chain(retriever)


    # --------------------------------------------------------
    # Store current resume pipeline in session state
    # --------------------------------------------------------

    st.session_state.documents = documents
    st.session_state.chunks = chunks
    st.session_state.vector_store = vector_store
    st.session_state.retriever = retriever
    st.session_state.rag_chain = rag_chain


    st.success(
        f"✅ {uploaded_file.name} processed successfully!"
    )

    st.info(
        f"Loaded {len(documents)} document(s) and "
        f"created {len(chunks)} chunks."
    )


# ============================================================
# RESUME Q&A
# ============================================================

if "rag_chain" in st.session_state:

    st.subheader("💬 Ask something about your resume")

    resume_question = st.text_input(
        "Resume question",
        placeholder="Example: What programming languages do I know?",
        key="resume_question"
    )

    if st.button(
        "Analyze Resume",
        key="resume_button"
    ):

        if resume_question:

            response = st.session_state.rag_chain.invoke(
                resume_question
            )

            st.subheader("🤖 Answer")

            st.write(response)

        else:

            st.warning(
                "Please enter a question about your resume."
            )

st.divider()

st.header("🎯 Job Description Matcher")

job_description = st.text_area(
    "Paste the Job Description",
    placeholder="Paste the job description here..."
)

if st.button("Match Resume with Job"):

    if "documents" not in st.session_state:
        st.warning("Please upload your resume first.")

    elif not job_description:
        st.warning("Please enter a job description.")

    else:

        resume_text = "\n\n".join(
            doc.page_content
            for doc in st.session_state.documents
        )

        job_match_chain = create_job_match_chain()

        result = job_match_chain.invoke(
            {
                "resume": resume_text,
                "job_description": job_description
            }
        )

        st.subheader("📊 Job Match Analysis")

        st.write(result)
