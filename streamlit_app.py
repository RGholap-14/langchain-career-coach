import streamlit as st
from app.chains.career_chain import career_chain
st.title("🚀 LangChain Career Coach")

question = st.text_area("Ask a career-related question")

if st.button("Ask"):
    response = career_chain.invoke(
        {
            "question": question
        }
    )

    st.write(response)