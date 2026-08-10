from langchain_core.prompts import ChatPromptTemplate


job_match_prompt = ChatPromptTemplate.from_template(
    """
You are an expert technical recruiter.

Compare the candidate's resume with the job description.

Resume:
{resume}

Job Description:
{job_description}

Provide the following:

1. Match Score: give a percentage from 0-100.
2. Matching Skills: list skills found in both.
3. Missing Skills: list important job requirements missing from the resume.
4. Recommendations: suggest what the candidate should improve.

Be concise and factual. Do not invent skills that are not present in the resume.
"""
)