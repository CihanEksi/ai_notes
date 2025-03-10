# %pip install streamlit
# %pip install langchain_community

import os
from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
modelName = "llama3.2:1b"

promptArray = [
    ("system", "You are a chatbot to answer questions."),
    ("user", "{question}"),
]


prompt = ChatPromptTemplate(
    promptArray,
)

llm = OllamaLLM(model=modelName)
output_parser = StrOutputParser()

## streamlit
st.title("LLMA Chat")
input_text = st.text_input("What question do you have?")

chain = prompt | llm | output_parser
chainObj = {"question": input_text}

if input_text:
    st.write(chain.invoke(chainObj))
