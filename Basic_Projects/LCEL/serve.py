# %pip install fastapi
# %pip install langserve
# %pip install sse_starlette
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

# Groq
groq_api_key = os.getenv("GROQ_API_KEY")
groqModelName = "llama-3.3-70b-versatile"
groqModel = ChatGroq(model=groqModelName, groq_api_key=groq_api_key)

# prompt
genericTemplate = "Translate the following sentences from {language} to Turkish"
messages = [
    ("system", genericTemplate),
    ("user", "{text}"),
]

prompt = ChatPromptTemplate.from_messages(
    messages,
)

parser = StrOutputParser()

# chain
chain = prompt | groqModel | parser


# rest api
app = FastAPI(title="Lang Chain Server", version="1.0", description="Lang Chain Server")

add_routes(app, chain, path="/translate")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
