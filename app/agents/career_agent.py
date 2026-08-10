from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from app.tools.job_tools import match_job_description


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


tools = [
    match_job_description
]


career_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a career assistant.

    Help the user with career-related questions.

    You have access to a tool that compares a resume
    with a job description.

    Use the tool when the user asks about job fit,
    matching a resume to a job description,
    missing skills, or job requirements.
    """
)