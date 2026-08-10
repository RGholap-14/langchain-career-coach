# 🚀 LangChain Career Coach

An AI-powered career assistant built with LangChain, Streamlit, OpenAI, ChromaDB, and Retrieval-Augmented Generation (RAG).

The application helps users:

- Ask general career-related questions
- Upload and ask questions about their resume
- Compare their resume against a job description
- Identify matching and missing skills

---

## 🏗️ Architecture

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

✨ Features
💼 1. Career Coach

Users can ask general career-related questions and receive AI-generated career guidance.

Example:

How can I prepare for a Python interview?
📄 2. Resume Assistant

Users can upload a PDF or DOCX resume and ask questions about their resume.

The application:

Loads the document
Splits the document into chunks
Generates embeddings
Stores embeddings in ChromaDB
Retrieves relevant chunks
Generates an answer using RAG

Example questions:

What programming languages do I know?
How many years of experience do I have?
What projects are mentioned in my resume?
🎯 3. Job Description Matcher

Users can paste a job description and compare it against their uploaded resume.

The Career Agent analyzes:

Matching skills
Missing skills
Relevant experience
Job fit
Recommendations

The job matching functionality uses a LangChain Agent and Tool.

🛠️ Tech Stack
Python
LangChain
LangChain OpenAI
OpenAI
Streamlit
ChromaDB
Python-dotenv
PDF/DOCX document loaders


🧠 LangChain Concepts Demonstrated
This project demonstrates practical LangChain concepts including:

Document Loaders
Text Splitting
Embeddings
Vector Stores
Retrievers
Retrieval-Augmented Generation (RAG)
Prompt Templates
LCEL Chains
LangChain Tools
Tool Calling
Agents
Streamlit integration


📁 Project Structure
langchain-career-coach/
│
├── app/
│   │
│   ├── agents/
│   │   └── career_agent.py
│   │
│   ├── chains/
│   │   ├── career_chain.py
│   │   ├── rag_chain.py
│   │   └── job_match_chain.py
│   │
│   ├── prompts/
│   │   ├── rag_prompt.py
│   │   └── job_match_prompt.py
│   │
│   ├── rag/
│   │   ├── loaders.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   └── tools/
│       └── job_tools.py
│
├── data/
│
├── .env
├── .gitignore
├── requirements.txt
├── streamlit_app.py
└── README.md


⚙️ Setup
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd langchain-career-coach
2. Create a virtual environment

For Windows:

python -m venv venv
3. Activate the virtual environment
.\venv\Scripts\Activate.ps1

You should see:

(venv)

at the beginning of your terminal prompt.

4. Install dependencies
pip install -r requirements.txt
🔐 Configure OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Replace:

your_api_key_here

with your actual OpenAI API key.


⚠️ Security
Never commit your .env file to GitHub.
Make sure .gitignore contains:

.env
venv/
__pycache__/
data/vector_store/


▶️ Run the Application
Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Then start Streamlit:

streamlit run streamlit_app.py

The application will open in your browser.

🖥️ Application

The application contains three main sections:

Career Coach
💼 Career Coach

Ask general career-related questions.

Resume Assistant
📄 Resume Assistant

Upload a PDF or DOCX resume and ask questions about it.

Job Description Matcher
🎯 Job Description Matcher

Upload your resume, paste a job description, and receive an AI-powered job match analysis.

🔄 RAG Pipeline

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
🤖 Agent Pipeline

The job matcher follows this pipeline:

Resume
   +
Job Description
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
💡 Example Workflow
Step 1

Open the application.

Step 2

Ask a career question:

How can I prepare for a Python interview?
Step 3

Upload your resume.

Step 4

Ask:

What technical skills do I have?
Step 5

Paste a job description.

Step 6

Click:

Match Resume with Job

The application generates an analysis of how well the resume matches the job description.

🚧 Future Improvements
Possible future improvements include:

PostgreSQL persistence
Dockerization
Conversation memory
User authentication
Job application tracking
Structured JSON output
Improved job matching scores
Resume improvement suggestions
Cloud deployment
Automated resume-to-job recommendations

📌 Project Status
Current implementation includes:

✅ LangChain Career Chat
✅ Resume Document Loading
✅ Text Splitting
✅ OpenAI Embeddings
✅ ChromaDB Vector Store
✅ Resume RAG
✅ Resume Q&A
✅ Job Description Matcher
✅ LangChain Tool
✅ Career Agent
✅ Streamlit UI

👩‍💻 Author
Rutuja
