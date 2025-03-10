# SimpleGenAiApp

This project demonstrates how to use LangChain and OpenAI's GPT-3.5-turbo model to create a simple AI application. The application includes web scraping, text splitting, embedding generation, and querying a vector store.

## Installation

To install the required packages, run the following commands:

```sh
%pip install langchain
%pip install python-dotenv
%pip install langchain-openai
%pip install beautifulsoup4
%pip install faiss-cpu
```

## Usage

1. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenAI and LangChain API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   ```

2. **Run the Jupyter Notebook**:
   Open `SimpleGenAiApp.ipynb` in Jupyter Notebook and execute the cells step by step.

### Steps in the Notebook

1. **Install dependencies**:
   The first cell installs the required Python packages.

2. **Load environment variables**:
   The second cell loads the environment variables from the `.env` file.

3. **Data ingestion**:
   The third cell demonstrates how to load and split documents from a web link.

4. **Generate embeddings**:
   The fourth cell generates embeddings for the split documents and stores them in a FAISS vector store.

5. **Query the vector store**:
   The fifth cell shows how to query the vector store for similar documents.

6. **Set up the language model**:
   The sixth cell initializes the ChatOpenAI model.

7. **Create a document chain**:
   The seventh cell creates a document chain using a prompt template.

8. **Manual document testing**:
   The eighth cell tests the model with a manually created document.

9. **Create a retrieval chain**:
   The ninth cell creates a retrieval chain combining the retriever and document chain.

10. **Get the response**:
    The tenth cell queries the retrieval chain and prints the response.

## License

This project is licensed under the MIT License.
