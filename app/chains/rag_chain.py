from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.models.llm import llm


rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AI Career Coach.

Answer the user's question using the resume context below.

If the answer is present in the context, answer it directly.

If the answer is not present in the context, say:
"I couldn't find that information in the uploaded resume."

Resume Context:
{context}
"""
    ),
    (
        "human",
        "{question}"
    ),
])


def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )


def create_rag_chain(retriever):

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x,
        }
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    return chain