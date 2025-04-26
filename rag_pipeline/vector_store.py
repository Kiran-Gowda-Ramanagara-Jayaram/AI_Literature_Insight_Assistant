from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def build_vector_store(documents, persist_directory="chroma_index"):
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectordb = Chroma.from_documents(documents, embedding, persist_directory=persist_directory)
    vectordb.persist()
    return vectordb


def load_vector_store(persist_directory="chroma_index"):
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)
