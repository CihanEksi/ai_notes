import streamlit as st
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")  
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
model_name = "Llama3-8b-8192"

st.title("RAG PDF Document And Chat History Search")
st.write(
    "This app uses the RAG model to search through a PDF document and chat history"
)
st.write("Please upload a PDF document and chat history to get started")

api_key = st.text_input("Enter your GROQ API Key", type="password")
llm = None


def get_session_history(session: str) -> BaseChatMessageHistory:
    if session not in st.session_state.store:
        st.session_state.store[session] = ChatMessageHistory()
    return st.session_state.store[session]


if api_key:
    llm = ChatGroq(model="Llama3-8b-8192",api_key=api_key)   # type: ignore

    sessionId = st.text_input("Enter your session ID", value="default_session")

    if "store" not in st.session_state:
        st.session_state.store = {}

    uploaded_files = st.file_uploader(
        "Choose a PDF document", type="pdf", accept_multiple_files=True
    )
    if uploaded_files:
        documents = []
        for uploaded_file in uploaded_files:
            tempPdf = f"./temp.pdf"
            with open(tempPdf, "wb") as f:
                f.write(uploaded_file.getvalue())
                file_name = f.name
            st.write(f"Uploaded {file_name}")
            loader = PyPDFLoader(tempPdf)
            loaded_documents = loader.load()
            documents.extend(loaded_documents)

        textSplitter = RecursiveCharacterTextSplitter(
            chunk_size=5000, chunk_overlap=500
        )
        splits = textSplitter.split_documents(documents)
        vectorStore = Chroma.from_documents(documents=splits, embedding=embeddings)
        retriever = vectorStore.as_retriever()

        systemPrompt = "Answer the following questions about the document:"

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", systemPrompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        history_aware_retriever = create_history_aware_retriever(llm, retriever, prompt)

        answerSystemPrompt = (
            "Answer the following questions about the document:"
            "<context>"
            "{context}"
            "</context>"
        )

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", answerSystemPrompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        document_chain = create_stuff_documents_chain(llm, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, document_chain)

        runnableRagChain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

        user_input = st.text_input("Enter your question")
        if user_input:
            sessionHistory = get_session_history(sessionId)
            response = runnableRagChain.invoke(
                {
                    "input": user_input,
                    "context": documents,
                },
                config={"configurable": {"session_id": sessionId}},
            )
            st.write(st.session_state.store)
            st.write("Assistant:", response["answer"])
            st.write("Chat History:", sessionHistory.messages)
else:
    st.write("Please enter your GROQ API Key")