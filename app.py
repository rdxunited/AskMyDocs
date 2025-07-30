import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import os
import tempfile

st.set_page_config(page_title="AskMyDocs 📄", layout="centered")

st.title("📄 AskMyDocs")
st.subheader("Private PDF Q&A using Local LLMs (Ollama + Langchain)")

# Upload file
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# Input box
query = st.text_input("Ask a question about the document")

if uploaded_file and query:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Load & split PDF
    loader = PyPDFLoader(tmp_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Embed & Index (limit to first 10 chunks for speed)
    embedding = OllamaEmbeddings(model="llama2")
    db = FAISS.from_documents(docs[:10], embedding)

    # Create Retrieval QA chain
    llm = Ollama(model="llama2")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever(), chain_type="stuff")

    # Run QnA
    with st.spinner("Thinking..."):
        result = qa.run(query)

    st.success("Answer:")
    st.write(result)
