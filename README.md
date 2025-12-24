├── 1. Project Overview
├── 2. System Architecture
├── 3. Technology Stack
├── 4. Authentication & Security
├── 5. Backend API Design
├── 6. n8n Workflow Explanation
├── 7. RAG Implementation
├── 8. Database Schema
├── 9. How to Run (Without Docker)
├── 10. Docker Setup (Optional)
├── 11. Limitations & Assumptions
├── 12. Demo Walkthrough


# Academic Assignment Helper & Plagiarism Detector

This project is a backend-focused academic assignment analysis system.
It allows students to upload assignments securely, analyzes the content using AI and Retrieval-Augmented Generation (RAG), detects potential plagiarism, and stores structured results in a PostgreSQL database.

The system is designed with a microservice mindset:
- FastAPI handles authentication, file uploads, and API access
- n8n orchestrates text extraction, AI analysis, RAG retrieval, and persistence
- PostgreSQL with pgvector is used for relational and vector-based storage


## System Architecture

1. Student authenticates using JWT-based authentication
2. Assignment file is uploaded via FastAPI
3. FastAPI saves the file and triggers an n8n webhook
4. n8n workflow:
   - Reads assignment file
   - Extracts text content
   - Performs AI-based academic analysis
   - Retrieves relevant academic sources using RAG
   - Computes plagiarism similarity scores
   - Stores structured results in PostgreSQL
5. Student retrieves analysis results via secured API endpoints


## Technology Stack

Backend:
- Python (FastAPI)
- JWT Authentication (python-jose)
- SQLAlchemy ORM

Automation:
- n8n (workflow orchestration)

Database:
- PostgreSQL
- pgvector (vector similarity search)

AI:
- OpenAI GPT models for analysis
- Embeddings for RAG-based retrieval

Infrastructure:
- Docker & Docker Compose (provided, optional)
## Authentication & Security

- JWT-based authentication is implemented
- Endpoints protected with role-based access
- Public endpoints:
  - POST /auth/register
  - POST /auth/login
- Protected endpoints:
  - POST /upload
  - GET /analysis/{id}
  - GET /sources

JWT tokens are required for all assignment-related operations.
## Backend API Design

POST /auth/register  
Registers a new student (simplified for demo purposes)

POST /auth/login  
Authenticates student and returns JWT token

POST /upload  
- Accepts assignment file
- Saves file locally
- Triggers n8n webhook for analysis
- Returns analysis job ID

GET /analysis/{id}  
Retrieves structured analysis results for a specific assignment


## n8n Workflow Explanation

The n8n workflow automates the entire assignment analysis pipeline.

Workflow Steps:
1. Webhook trigger receives file path and metadata from FastAPI
2. Assignment file is read from disk
3. Text content is extracted using a Python node
4. Text is preprocessed and truncated for token limits
5. OpenAI model analyzes:
   - Assignment topic
   - Academic level
   - Key themes
   - Research questions
   - Citation recommendations
6. RAG-based retrieval fetches relevant academic sources
7. Plagiarism similarity score is computed
8. Final structured analysis is stored in PostgreSQL

The workflow is exported as:
workflows/assignment_analysis_workflow.json
## RAG (Retrieval-Augmented Generation)

Academic materials are stored in PostgreSQL using pgvector embeddings.

RAG Pipeline:
1. Academic documents are chunked and embedded
2. Assignment text is embedded at query time
3. Cosine similarity search retrieves top-k relevant sources
4. Retrieved context is used to enhance AI analysis

This approach improves factual grounding and source relevance.
## Database Schema

Main tables:
- students
- assignments
- analysis_results
- academic_sources

Vector embeddings are stored using pgvector for similarity search.
