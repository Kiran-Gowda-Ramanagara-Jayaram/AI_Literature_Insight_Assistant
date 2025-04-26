from langchain.chains import RetrievalQA, load_summarize_chain
from langchain.chat_models import ChatOpenAI

# Query the vector store with LLM context retrieval
def query_with_context(vectorstore, query):
    llm = ChatOpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa.run(query)

# Summarize a document using map-reduce chain
def summarize_document(docs):
    llm = ChatOpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)