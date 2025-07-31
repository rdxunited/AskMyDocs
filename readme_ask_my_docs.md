# AskMyDocs – Chat with Your Documents using Generative AI

## 👥 Team Members

- Mihir Kiroriwal
- Mayank Kumawat
- Ayush Pareek

## 📌 Project Overview

**AskMyDocs** is a Generative AI-based document assistant that allows users to upload any PDF document and ask questions about its content. The app uses local LLMs through Ollama and processes document content using LangChain and FAISS for efficient information retrieval.

## 🚀 Features

- Upload PDF documents
- Automatic chunking of text
- Generate embeddings with Ollama (LLaMA2)
- Vector storage and retrieval with FAISS
- Answer user queries based on document context

## 🧠 Tech Stack

- Python 3.11
- Jupyter Notebook (.ipynb)
- LangChain
- FAISS
- Ollama (LLaMA2)

## 📁 Project Structure

```
AskMyDocs/
├── AskMyDocs.ipynb     # Main Jupyter Notebook
├── sample.pdf          # Sample PDF for testing
├── requirements.txt    # Required dependencies
├── .env                # Optional: API keys (if needed)
├── README.md           # Project documentation
```

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/rdxunited/AskMyDocs.git
cd AskMyDocs
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Notebook**

- Open `AskMyDocs.ipynb` in Jupyter Notebook or JupyterLab
- Execute cells step by step

4. **Load Your Own PDF**

- Replace `sample.pdf` with your own document
- Ask relevant questions in the chat cell

## 💡 Notes

- This app runs locally and does not require internet after model installation.
- Performance depends on the size of the PDF and the model used.
- For smoother performance, try smaller PDFs during testing.

## 📚 Example Use Case

Upload `Rich Dad Poor Dad.pdf` and ask:

> "What is the main difference between assets and liabilities according to the author?"

## 📢 Acknowledgements

- LangChain for document parsing and chaining
- FAISS for vector search
- Ollama for running local LLMs

---

**Made with collaboration by Mihir Kiroriwal, Mayank Kumawat, and Ayush Pareek**

