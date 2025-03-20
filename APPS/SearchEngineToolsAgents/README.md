# Search Engine Tools Agents

This application is a Streamlit-based chatbot that integrates multiple search tools to provide detailed answers to user queries. It leverages LangChain's capabilities to interact with APIs like DuckDuckGo, Wikipedia, and Arxiv, and uses a Groq-powered language model for generating responses.

## Features

- **DuckDuckGo Search**: Perform web searches for real-time information.
- **Wikipedia Query**: Retrieve detailed information from Wikipedia.
- **Arxiv Query**: Search academic papers and research articles from Arxiv.
- **Chat Interface**: Interactive chat interface powered by Streamlit.
- **Customizable Model**: Uses the `Llama3-8b-8192` model for generating responses.

## Requirements

- Python 3.8 or higher
- Streamlit
- LangChain and its community tools
- HuggingFace Embeddings
- FAISS for vector storage
- dotenv for environment variable management

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SearchEngineToolsAgents
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your environment variables:
   ```
   GROQ_API_KEY=<your_groq_api_key>
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser at `http://localhost:8501`.

3. Enter your Groq API key in the sidebar and start interacting with the chatbot.

## Configuration

- **Model Name**: The default model is `Llama3-8b-8192`. You can modify this in the `app.py` file.
- **Search Tools**: The application uses DuckDuckGo, Wikipedia, and Arxiv by default. You can add or remove tools in the `tools` list in `app.py`.

## Troubleshooting

- Ensure all dependencies are installed.
- Verify your Groq API key is correct and active.
- Check the `.env` file for proper configuration.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [Streamlit](https://streamlit.io/)
- [DuckDuckGo](https://duckduckgo.com/)
- [Wikipedia](https://www.wikipedia.org/)
- [Arxiv](https://arxiv.org/)
