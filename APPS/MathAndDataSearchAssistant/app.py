from tabnanny import verbose
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from dotenv import load_dotenv
import numexpr  # Add this import for evaluating math expressions

load_dotenv()


## Streamlit

st.set_page_config(
    page_title="Math and Data Search Assistant", page_icon="📊", layout="wide"
)

st.title("Math and Data Search Assistant")
st.subheader("Search for math and data related information and get answers!")

groq_api_key = st.sidebar.text_input("Groq API Key", type="password", value='')

if not groq_api_key:
    st.error("Please enter Groq API Key")
    st.stop()

modelName = "Llama3-8b-8192"

llm = ChatGroq(model=modelName, api_key=groq_api_key)  # type: ignore

wikipediaWrapper = WikipediaAPIWrapper(wiki_client=None)

wikipediaTool = Tool(
    name="Wikipedia",
    func=wikipediaWrapper.run,
    description="Search Wikipedia for information",
)

# Update the mathChain initialization to include error handling
mathChain = LLMMathChain.from_llm(llm=llm, verbose=True)

# Update the Calculator tool to handle math expressions safely
def safe_calculate(query):
    try:
        if not query.strip():
            return "Invalid input"
        # Use numexpr to evaluate the math expression
        result = numexpr.evaluate(query)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

calculater = Tool(
    name="Calculator",
    func=safe_calculate,
    description="Calculate math expressions",
)

promt = """
    You are agent tasked for solving math and data related queries.
    Question: {question}
"""

promptTemplate = PromptTemplate(template=promt, input_variables=["question"])

## combine all tools to chain
chain = promptTemplate | llm


reasonTool = Tool(
    name="Reasoning",
    func=chain.invoke,
    description="Reasoning with the model",
)

## initialize agent

assistant_agent = initialize_agent(
    llm=llm,
    tools=[wikipediaTool, calculater, reasonTool],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# Update the generate_response function to handle unexpected LLM responses
def generate_response(userQuestion):
    try:
        response = assistant_agent.invoke({
            "input": userQuestion
        })
        # Ensure the response is a string and handle unexpected formats
        if not isinstance(response, str):
            raise ValueError("Unexpected response format from LLM")
        return response
    except ValueError as e:
        return f"An error occurred: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hello! I am your assistant. How can I help you today?",
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

question = st.text_input("Ask me anything!","if a=2 and b=3, what is a+b?")


# Update the response generation in the Streamlit button click handler
if st.button("Ask"):
    if not question:
        st.error("Please enter a question")
        st.stop()
    with st.spinner("Thinking..."):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )
        st.chat_message("user").write(question)
        st_callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        try:
            response = assistant_agent.run(
                st.session_state.messages,
                callbacks=[st_callback],
            )
            # Ensure the response is valid
            if not isinstance(response, str):
                raise ValueError("Unexpected response format from LLM")
        except ValueError as e:
            response = f"An error occurred: {str(e)}"
        except Exception as e:
            response = f"An unexpected error occurred: {str(e)}"

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )
        print(response)
        st.write("Response:")
        st.success(response)