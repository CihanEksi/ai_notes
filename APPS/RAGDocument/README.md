# RAG Document Search

This project implements a Retrieval-Augmented Generation (RAG) system for document search using LangChain. It allows users to upload PDF documents, create embeddings, and perform similarity-based searches with a question-answering interface.

## Features

- **Document Embedding**: Converts PDF documents into vector embeddings using OpenAI embeddings.
- **Question Answering**: Answers user queries based on the uploaded documents.
- **Similarity Search**: Retrieves document chunks most relevant to the user's query.
- **Streamlit Interface**: Provides a user-friendly web interface for interaction.

## Requirements

Ensure you have the following installed:

- Python 3.8 or higher
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RAGDocument
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file:
   - Add your API keys for OpenAI, LangSmith, and Groq.
   - Example:
     ```
     OPENAI_API_KEY='your-openai-api-key'
     GROQ_API_KEY='your-groq-api-key'
     ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser (default: `http://localhost:8501`).

3. **Steps to Use**:
   - Click the "Document Attachment" button to upload and embed documents.
   - Enter a query in the text input field and press Enter.
   - View the answer and similar document chunks in the interface.

## Project Structure

- `app.py`: Main application file for the Streamlit interface.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables for API keys.
- `research_papers/`: Directory to store PDF documents for processing.

## Troubleshooting

- **Missing API Keys**: Ensure all required API keys are set in the `.env` file.
- **No Documents Found**: Place your PDF files in the `research_papers/` directory.
- **KeyError**: Ensure the input key matches the expected parameter in the chain.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
