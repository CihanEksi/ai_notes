import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader

## Prompt
prompt_template = """
    Provide a summary of the following content and translate summary to this language {lang}:
    {text}
"""
prompt = PromptTemplate(template=prompt_template,input_variables=["text","lang"])

## GROQ
model_name = "Llama3-8b-8192"

## Streamlit
st.set_page_config(page_title="Text Summarization",page_icon="📝",layout="wide")
st.title("Text Summarization")
st.subheader("Summarize any text or video content with url!")


with st.sidebar:
    groq_api_key = st.text_input("Groq API Key",type="password",value='')

url = st.text_input("Enter URL",label_visibility="collapsed")


if st.button("Summarize"):

    if not validators.url(url):
        st.error("Invalid URL to Summarize")
        st.stop()
    
    if not groq_api_key:
        st.error("Please enter Groq API Key")
        st.stop()

    llm = ChatGroq(api_key=groq_api_key, model=model_name)  # type: ignore

    try:
        st.spinner("Summarizing...")
        
        if "youtube.com" in url:
            try:
                loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                data = loader.load()
            except Exception as youtube_error:
                st.error(f"Failed to load YouTube video: {youtube_error}")
                st.stop()
        else:
            loader = UnstructuredURLLoader(urls=[url], ssl_verify=False, header={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            })
            data = loader.load()

        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)

        # Ensure you have the input_documents prepared
        input_documents = data  # Replace with your actual documents or data

        summary = chain.invoke(input={
            "input_documents": input_documents,
            "text": data,
            "lang": "Turkish"
        })

        st.success(summary["output_text"])
    except Exception as e:
        st.exception(e)
        st.error("Failed to summarize content")
        st.stop()