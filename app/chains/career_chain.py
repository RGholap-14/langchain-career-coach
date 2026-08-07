from langchain_core.output_parsers import StrOutputParser

from app.models.llm import llm
from app.prompts.career_prompt import career_prompt

parser = StrOutputParser()

career_chain = career_prompt | llm | parser