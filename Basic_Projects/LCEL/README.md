# LCEL Project

This project demonstrates how to use LangChain with Groq and OpenAI models to create a language translation application. The application includes setting up model environments, invoking models, and chaining components.

## Installation

To install the required packages, run the following commands:

```sh
%pip install langchain
%pip install langchain_groq
%pip install langchain_core
%pip install openai
%pip install fastapi
%pip install langserve
%pip install sse_starlette
```

## Usage

1. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenAI and Groq API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

2. **Run the Jupyter Notebook**:
   Open `ChatGroq.ipynb` in Jupyter Notebook and execute the cells step by step.

### Steps in the Notebook

1. **Install dependencies**:
   The first cell installs the required Python packages.

2. **Load environment variables**:
   The second cell loads the environment variables from the `.env` file.

3. **Set up model environments**:
   The third cell sets up the OpenAI and Groq model environments.

4. **Invoke the model**:
   The fourth cell demonstrates how to invoke the Groq model with a translation task.

5. **Parse the output**:
   The fifth cell shows how to parse the output of the model.

6. **Chain components**:
   The sixth cell demonstrates how to chain the model and parser components.

7. **Create a prompt template**:
   The seventh cell creates a prompt template for translation.

8. **Invoke the prompt**:
   The eighth cell shows how to invoke the prompt with input data.

9. **Chain the prompt, model, and parser**:
   The ninth cell demonstrates how to chain the prompt, model, and parser components.

3. **Run the FastAPI server**:
   Open `serve.py` and run the FastAPI server to expose the translation chain as an API.

### Steps in the FastAPI Server

1. **Set up environment variables**:
   The first part of the script loads the environment variables from the `.env` file.

2. **Initialize the Groq model**:
   The second part initializes the Groq model with the API key and model name.

3. **Create a prompt template**:
   The third part creates a prompt template for translation.

4. **Create a chain**:
   The fourth part chains the prompt, model, and parser components.

5. **Set up the FastAPI app**:
   The fifth part sets up the FastAPI app and adds routes for the translation chain.

6. **Run the server**:
   The last part runs the FastAPI server on `localhost:8000`.

## License

This project is licensed under the MIT License.
