# RAGDocumentAstraDB

This project demonstrates how to use LangChain with AstraDB to create a Retrieval-Augmented Generation (RAG) system for document-based question answering. The system processes a PDF document, stores its content in a vector database, and allows users to query the document using natural language.

## Features

- Extracts text from PDF documents.
- Splits text into manageable chunks for vector storage.
- Uses OpenAI embeddings for vectorization.
- Stores vectors in AstraDB.
- Provides a conversational interface for querying the document.

## Prerequisites

- Python 3.8 or higher
- AstraDB account and credentials
- OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd RAGDocumentAstraDB
   ```

2. Install the required Python packages:
   ```bash
   pip install cassio datasets langchain astrapy langchain-openai tiktoken cassandra-driver PyPDF2 langchain-community --quiet --user
   ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add the following variables:
     ```
     ASTRA_DB_APPLICATION_TOKEN=<your_astra_db_application_token>
     ASTRA_DB_ID=<your_astra_db_id>
     OPENAI_API_KEY=<your_openai_api_key>
     ```

## Usage

1. Place the PDF file you want to process in the project directory and name it `sample.pdf`.

2. Open the `astraDB.ipynb` notebook and run the cells sequentially:
   - Install dependencies.
   - Load environment variables.
   - Extract text from the PDF.
   - Initialize AstraDB and OpenAI embeddings.
   - Split the text into chunks and store them in the vector database.
   - Query the document interactively.

3. Start asking questions about the document in the interactive prompt.

## Notes

- Ensure your AstraDB and OpenAI credentials are valid.
- Modify the `chunk_size` and `chunk_overlap` parameters in the text splitter to suit your document's structure.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

