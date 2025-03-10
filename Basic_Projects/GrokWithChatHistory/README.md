# GrokWithChatHistory Project

This project demonstrates how to use LangChain with Groq models to create an AI application that maintains chat history. The application includes setting up model environments, invoking models, and managing chat history.

## Installation

To install the required packages, run the following commands:

```sh
%pip install langchain
%pip install langchain_groq
%pip install langchain_core
%pip install langchain_community
```

## Usage

1. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

2. **Run the Jupyter Notebook**:
   Open `grok.ipynb` in Jupyter Notebook and execute the cells step by step.

### Steps in the Notebook

1. **Install dependencies**:
   The first cell installs the required Python packages.

2. **Load environment variables**:
   The second cell loads the environment variables from the `.env` file.

3. **Set up model environments**:
   The third cell sets up the Groq model environment.

4. **Invoke the model**:
   The fourth cell demonstrates how to invoke the Groq model with a chat history.

5. **Manage chat history**:
   The fifth cell shows how to manage chat history using `ChatMessageHistory`.

6. **Generate session ID**:
   The sixth cell generates a unique session ID for each chat session.

7. **Invoke the model with session history**:
   The seventh cell demonstrates how to invoke the model with session history.

8. **Use prompt templates**:
   The eighth cell shows how to use prompt templates with the model.

9. **Trim messages**:
   The ninth cell demonstrates how to trim messages to fit within a token limit.

10. **Use vector store**:
    The tenth cell shows how to use a vector store for document retrieval.

11. **Retrieve documents**:
    The eleventh cell demonstrates how to retrieve documents using the vector store.

12. **RAG (Retrieval-Augmented Generation)**:
    The twelfth cell shows how to use RAG to answer questions based on retrieved documents.

## License

This project is licensed under the MIT License.
