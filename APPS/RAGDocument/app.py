from tkinter.font import BOLD
from venv import create
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import time

load_dotenv()

## load the groq api
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
grok_api_key = os.getenv("GROQ_API_KEY")
model_name = "Llama3-8b-8192"
loaderDir = "research_papers"

llm = ChatGroq(model_name=model_name)
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following questions about the document:
    <context>
    {context}
    </context>
    Question: {input}
"""
)

def create_vector_embedding():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        st.session_state.loader = PyPDFDirectoryLoader(loaderDir)
        st.session_state.docs = st.session_state.loader.load()
        
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("RAG Document Search")
user_prompt = st.text_input("Enter the prompt")

if st.button("Document Attachment"):
    create_vector_embedding()
    if 'vectors' in st.session_state:
        st.write("Document Embedding Done")
    else:
        st.write("Document Embedding Failed")

if user_prompt:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retriever_chain.invoke({
        "input": user_prompt  
    })
    st.write(response['answer'],BOLD)
    finalTime = time.process_time() - start
    
    print(f'Response time: {finalTime}')
    with st.expander("Document Similarity search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("------------------")

