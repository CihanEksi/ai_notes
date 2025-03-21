from gc import callbacks
from httpx import stream
import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from mysql import connector


st.set_page_config(page_title="SQL Chat", page_icon=":bar_chart:")
st.title("SQL Chat")

LOCALDB = "USE_LOCAL_DB"
MYSQL = "USE_MYSQL"

radioButton = ["Use SQL3 Database", "Connect to your Database"]
selectedDB = st.sidebar.radio(label="Select Database", options=radioButton)
model_name = "Llama3-8b-8192"
mysqlHost = None
mysqlUser = None
mysqlPassword = None
mysqlDb = None
db_uri = None

if selectedDB == radioButton[1]:
    db_uri = MYSQL
    mysqlHost = st.sidebar.text_input("Enter MySQL Host", "localhost")
    mysqlUser = st.sidebar.text_input("Enter MySQL User", "root")
    mysqlPassword = st.sidebar.text_input("Enter MySQL Password", type="password")
    mysqlDb = st.sidebar.text_input("Enter MySQL Database", "employees")
else:
    db_uri = LOCALDB

api_key = st.sidebar.text_input("Enter GROQ API Key",'', type="password")

if not db_uri:
    st.warning("Please select a database")

if not api_key:
    st.warning("Please enter a GROQ API Key")

## LLM Setup
llm = ChatGroq(api_key=api_key, model=model_name)  # type: ignore


@st.cache_resource(ttl=3600)
def configure_db(
    db_uri, mysql_host=None, sqlPassword=None, mysql_db=None, mysql_user=None
):
    if db_uri == MYSQL:
        if not mysql_host or not mysql_db or not mysql_user:
            st.warning("Please enter all the MySQL details")
            st.stop()
        try:
            engine = create_engine(
                f"mysql+mysqlconnector://{mysql_user}:{sqlPassword}@{mysql_host}/{mysql_db}"
            )
        except Exception as e:
            st.error(f"Failed to connect to MySQL database: {e}")
            st.stop()
        return SQLDatabase(engine)
    elif db_uri == LOCALDB:
        dfFilePath = (Path(__file__).parent / "employees.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{dfFilePath}?mode=rwc", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))


db = configure_db(db_uri, mysqlHost, mysqlPassword, mysqlDb, mysqlUser)


toolkit = SQLDatabaseToolkit(db=db,llm=llm) # type: ignore

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True  # Enable error handling for output parsing
)

if "messages" not in st.session_state or st.sidebar.button('Clear message history'):
    st.session_state["messages"] = [{
        "role": "assistant",
        "content": "How can I help you?"
    }]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anthying about you interested in")

if user_query:
    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(input={
            "input": user_query
        },callbacks=[streamlit_callback])

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        st.write(response)

