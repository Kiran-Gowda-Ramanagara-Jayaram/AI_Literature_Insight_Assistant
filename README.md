# AI Literature Insight Assistant

An intelligent AI-driven assistant that helps researchers and students upload, summarize, analyze, and query academic research papers through a dynamic web interface.

---

## Features

- Multi-PDF Upload and parallel processing
- Dynamic Executive Summarization of papers
- Citation Extraction from uploaded documents
- Word Count and Estimated Reading Time Calculation
- Contextual Question-Answering from documents
- Beautiful Streamlit Frontend with dynamic Lottie Animations
- Q&A Transcript Download feature
- Modular, Production-Ready Code for easy expansion

---

## Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- FAISS (Facebook AI Similarity Search)
- OpenAI or HuggingFace Embeddings
- Unstructured (for PDF parsing)
- Streamlit-Lottie (for Animations)

---

## Project Structure

```plaintext
AI_Literature_Assistant/
├── app/
│   └── main.py                # Main Streamlit application
├── preprocessing/
│   └── pdf_parser.py           # Parsing and preprocessing of uploaded PDFs
├── rag_pipeline/
│   ├── vector_store.py         # Build and load vector database (FAISS)
│   └── llm_query.py            # Query retrieval and summarization with LLM
├── data/                       # Temporary storage for uploaded PDFs
├── faiss_index/                # Persistent FAISS vector indexes
└── requirements.txt            # Project dependencies
```

---

## Setup Instructions

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the Application:**
```bash
streamlit run app/main.py
```

---

## Usage Instructions

- Upload one or multiple academic PDFs.
- The app will:
  - Parse and chunk documents.
  - Build a vector database.
  - Summarize content dynamically.
  - Extract and list citations.
  - Calculate total word count and estimated reading time.
- Type a question related to the documents.
- Get contextual answers from your uploaded PDFs.
- Download the full Q&A session for your records.

---

## Acknowledgements

- Streamlit
- LangChain
- OpenAI / HuggingFace Embeddings
- FAISS
- LottieFiles for public animations

---

Designed and developed for academic research and real-world AI applications.
