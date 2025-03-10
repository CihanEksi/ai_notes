# Ollama Chat

This is a basic chatbot application built using Streamlit and Langchain. The chatbot uses the OllamaLLM model to answer user questions.

## Installation

To install the required packages, run the following commands:

```bash
pip install streamlit
pip install langchain_community
```

## Usage

1. Set up your environment variables in a `.env` file:
    ```
    LANGSMITH_API_KEY=your_api_key
    LANGCHAIN_PROJECT=your_project_name
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run SimpleOllamaChat.py
    ```

3. Open your browser and go to `http://localhost:8501` to interact with the chatbot.

## Files

- `SimpleOllamaChat.py`: The main script to run the chatbot.
- `readMe.md`: This README file.

## License

This project is licensed under the MIT License.
