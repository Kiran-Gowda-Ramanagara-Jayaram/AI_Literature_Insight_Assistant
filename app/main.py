import sys
import os
import streamlit as st
import time
import requests
from langchain.schema import Document
from streamlit_lottie import st_lottie

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import custom modules
from preprocessing.pdf_parser import parse_pdf, extract_citations, get_text_metrics
from rag_pipeline.vector_store import build_vector_store, load_vector_store
from rag_pipeline.llm_query import query_with_context, summarize_document

# Set Streamlit page configuration
st.set_page_config(page_title="AI Literature Insight Assistant")

# Load Lottie Animation
@st.cache_data(show_spinner=False)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ Use a real public JSON animation (no expiration)
lottie_url = "https://assets1.lottiefiles.com/packages/lf20_tno6cg2w.json"
lottie_animation = load_lottie_url(lottie_url)

# Display animation
if lottie_animation:
    st_lottie(lottie_animation, height=300, speed=1, loop=True)
else:
    st.info("📖 Welcome to AI Literature Insight Assistant")

# Main Title
st.title("AI Literature Insight Assistant")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []

# File uploader
uploaded_files = st.file_uploader("Upload research papers (PDF)", type=["pdf"], accept_multiple_files=True)

# Process uploaded files
if uploaded_files:
    all_documents = []
    full_texts = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Uploaded: {uploaded_file.name}")

        chunks = parse_pdf(file_path)
        all_documents.extend([Document(page_content=str(chunk)) for chunk in chunks])
        full_texts.extend([str(chunk) for chunk in chunks])

    with st.spinner("Analyzing your documents..."):
        time.sleep(1)
        vectordb = build_vector_store(all_documents)
        summary = summarize_document(all_documents)
        citations = extract_citations(" ".join(full_texts))
        total_words, estimated_time = get_text_metrics(full_texts)

        st.success("📚 Documents indexed successfully!")

        # Display document insights
        st.markdown("### Executive Summary")
        st.info(summary)

        st.markdown("### Paper Insights")
        st.metric("Total Words", total_words)
        st.metric("Estimated Reading Time (minutes)", estimated_time)
        st.metric("Number of Citations Extracted", len(citations))

        if citations:
            st.markdown("### Citations Found:")
            for c in citations:
                st.markdown(f"- Citation [{c}]")

# User question input
query = st.text_input("Enter your question about the uploaded papers:")

if query:
    vectordb = load_vector_store()
    response = query_with_context(vectordb, query)
    st.session_state.history.append((query, response))

    # Display answer
    st.markdown("### Answer")
    st.write(response)

    st.markdown("---")
    st.markdown("### Q&A History")
    for q, a in st.session_state.history[::-1]:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Assistant:** {a}")

    with st.expander("Download Q&A Session"):
        transcript = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in st.session_state.history])
        st.download_button("Download Transcript", transcript, file_name="qa_session.txt")
