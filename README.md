# 🚀 LangChain Career Coach

An AI-powered career assistant built with LangChain, Streamlit, OpenAI, ChromaDB, and Retrieval-Augmented Generation (RAG).

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Pipelines](#pipelines)
  - [RAG Pipeline](#rag-pipeline)
  - [Agent Pipeline](#agent-pipeline)
- [Future Improvements](#future-improvements)
- [Project Status](#project-status)
- [Author](#author)

---

## Features

The application helps users:

- Ask general career-related questions (Career Coach)
- Upload and ask questions about their resume (Resume Assistant)
- Compare a resume against a job description (Job Matcher)
- Identify matching and missing skills and receive recommendations


## Architecture

```text
                         Streamlit
                            │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
          Career Chat    Resume Assistant   Job Matcher
                │             │             │
                ▼             ▼             ▼
               LLM          RAG Chain    Career Agent
                              │             │
                              ▼             ▼
                           ChromaDB     Job Match Tool
                              │             │
                              └──────┬──────┘
                                     ▼
                                OpenAI LLM
```


## Tech Stack

- Python
- LangChain
- OpenAI (LLMs & Embeddings)
- Streamlit (UI)
- ChromaDB (vector store)
- python-dotenv
- PDF/DOCX document loaders


## Installation

1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd langchain-career-coach
```

2. Create a virtual environment

For Windows:

```bash
python -m venv venv
```

3. Activate the virtual environment (Windows PowerShell example)

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies

```bash
pip install -r requirements.txt
```


## Configuration

Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=your_api_key_here
```

Security: Never commit your `.env` file. Ensure `.gitignore` contains:

```
.env
venv/
__pycache__/
data/vector_store/
```


## Usage

Start the Streamlit application after activating your virtual environment:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser. The main sections are:

- Career Coach — Ask career questions (interview prep, career strategies, etc.)
- Resume Assistant — Upload a resume (PDF/DOCX) and ask questions about its content
- Job Description Matcher — Paste a job description and match it against the uploaded resume


## Project Structure

```
langchain-career-coach/
├── app/
│   ├── agents/
│   │   └── career_agent.py
│   ├── chains/
│   │   ├── career_chain.py
│   │   ├── rag_chain.py
│   │   └── job_match_chain.py
│   ├── prompts/
│   │   ├── rag_prompt.py
│   │   └── job_match_prompt.py
│   ├── rag/
│   │   ├── loaders.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   └── tools/
│       └── job_tools.py
├── data/
├── .env
├── .gitignore
├── requirements.txt
├── streamlit_app.py
└── README.md
```


## Pipelines

### RAG Pipeline

The resume assistant follows this pipeline:

Resume PDF/DOCX
   ↓
Document Loader
   ↓
Text Splitter
   ↓
Document Chunks
   ↓
OpenAI Embeddings
   ↓
ChromaDB Vector Store
   ↓
Retriever
   ↓
Relevant Context
   ↓
RAG Chain
   ↓
LLM
   ↓
Answer


### Agent Pipeline

The job matcher follows this pipeline:

Resume + Job Description
   ↓
Career Agent
   ↓
Job Match Tool
   ↓
Job Match Chain
   ↓
LLM
   ↓
Job Match Analysis


## Example Workflow

1. Open the application.
2. Ask a career question (e.g., "How can I prepare for a Python interview?").
3. Upload your resume.
4. Ask resume-specific questions (e.g., "What technical skills do I have?").
5. Paste a job description.
6. Click "Match Resume with Job" to get a job match analysis and recommendations.


## Future Improvements

- PostgreSQL persistence
- Dockerization
- Conversation memory
- User authentication
- Job application tracking
- Structured JSON output
- Improved job matching scores
- Resume improvement suggestions
- Cloud deployment
- Automated resume-to-job recommendations


## Project Status

Current implementation includes:

- ✅ LangChain Career Chat
- ✅ Resume Document Loading
- ✅ Text Splitting
- ✅ OpenAI Embeddings
- ✅ ChromaDB Vector Store
- ✅ Resume RAG
- ✅ Resume Q&A
- ✅ Job Description Matcher
- ✅ LangChain Tool
- ✅ Career Agent
- ✅ Streamlit UI


## Author

Rutuja
