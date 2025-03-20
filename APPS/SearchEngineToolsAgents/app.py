import streamlit as st
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent,AgentType
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)

import os
from dotenv import load_dotenv
load_dotenv()

doc_content_chars_max = 1000
top_k_results = 3
model_name = "Llama3-8b-8192"

tools = []

search = DuckDuckGoSearchRun(name="Search")
tools.append(search)

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=top_k_results,doc_content_chars_max=doc_content_chars_max,lang='en',wiki_client=None)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
tools.append(wiki)

api_wrapper_arxiv = ArxivAPIWrapper(arxiv_search=None,arxiv_exceptions=None,top_k_results=top_k_results,doc_content_chars_max=doc_content_chars_max)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
tools.append(arxiv)



st.title("Search Engine Tools Agents")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Groq API Key",type="password")


if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi I am a chatbot who can search the web and answer questions with deep details. Ask me anything!",
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input(placeholder="What is machine learning?")

if prompt and api_key:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
    st.chat_message("user").write(prompt)
    
    llm = ChatGroq(api_key=api_key,model=model_name,streaming=True) # type: ignore

    ## AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION chatbot dont care chat history just focusing the question
    ## AgentType.CHAT_ZERO_SHOT_REACT chatbot care chat history and focusing the question

    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )

    with st.chat_message('assistant'):
        stCallback = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)

        try:
            response = search_agent.run(st.session_state.messages, callbacks=[stCallback])
            print(response)
        except Exception as e:
            st.write(f"Error: {e}")
            response = "Sorry, I couldn't process your request."

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )
        st.write(response)