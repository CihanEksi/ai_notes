from click import prompt
import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
load_dotenv()


os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] =  'One Question'

### Settings
temperature = 0.5 ## yaraticilik
max_tokens = 100
model = "gpt-3.5-turbo" ## default model
outputParser = StrOutputParser()

openai_models = ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"]
ollama_models = ["llama3.2:1b", "phi3" ]

## Prompt Template
prompt= ChatPromptTemplate.from_messages([ 
    ('system','You are a helpful AI assistant. You are here to help me with my questions.'),
    ("user","{question}"),
    ]
)

def generate_response(question,selected_model,api_key):
    llm = OllamaLLM(model=selected_model,temperature=temperature,max_tokens=max_tokens)
    if selected_model in openai_models:
        openai.api_key = api_key
        llm = ChatOpenAI(model=selected_model,temperature=temperature,max_tokens=max_tokens)

    chain = prompt | llm | outputParser
    answer = chain.invoke({'question':question})
    return answer


## Streamlit

st.title('One Question')

st.sidebar.title('Settings')
api_key = st.sidebar.text_input('OpenAI API Key')


selectedModel = st.sidebar.selectbox(
    "Select Model",
    ollama_models + openai_models,
    index=0
)


temperature = st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.5,step=0.1)

max_tokens = st.sidebar.slider('Max Tokens',min_value=50,max_value=500,value=100,step=50)


user_input = st.text_input('You:')

if user_input:
    response = generate_response(user_input,selectedModel,os.getenv('LANGCHAIN_API_KEY'))
    st.write(response)
else:
    st.write('AI:')
    st.write('Ask me a question!')