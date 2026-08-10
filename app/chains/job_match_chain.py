from langchain_core.output_parsers import StrOutputParser

from app.models.llm import llm
from app.prompts.job_match_prompt import job_match_prompt


def create_job_match_chain():

    chain = (
        job_match_prompt
        | llm
        | StrOutputParser()
    )

    return chain    