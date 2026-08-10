from langchain_core.tools import tool

from app.chains.job_match_chain import create_job_match_chain


@tool
def match_job_description(
    resume: str,
    job_description: str
) -> str:
    """
    Compare a candidate resume with a job description
    and return a job match analysis.
    """

    job_match_chain = create_job_match_chain()

    result = job_match_chain.invoke(
        {
            "resume": resume,
            "job_description": job_description
        }
    )

    return result