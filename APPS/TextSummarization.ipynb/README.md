# Text Summarization with LangChain

This project demonstrates how to use the LangChain framework to summarize text using various chain types, including `Stuff`, `Map Reduce`, and `Refine`. It also showcases how to integrate with the `ChatGroq` model for generating summaries.

## Features

- Summarize text using different chain types (`Stuff`, `Map Reduce`, `Refine`).
- Translate summaries into different languages.
- Process and summarize PDF documents.
- Token counting for input text.
- Generate motivational titles and reader-friendly summaries.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install langchain langchain_groq langchain_community python-dotenv
   ```
3. Create a `.env` file in the root directory and add your `GROQ_API_KEY`:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
4. Place any PDF files you want to summarize in the project directory (e.g., `zucker.pdf`).

## Usage

1. Open the `text_summary.ipynb` notebook in Jupyter Notebook or JupyterLab.
2. Follow the cells step-by-step to:
   - Load and summarize text or PDF documents.
   - Use different chain types for summarization.
   - Translate summaries into other languages.
3. Customize the prompts and templates as needed.

## Example

### Summarizing a Speech
The notebook includes an example speech:
```python
speech = """On the one hand, [the iPhone has] been great, because now pretty much everyone in the world has a phone..."""
```
You can summarize it using the `ChatGroq` model and various chain types.

### Summarizing a PDF
To summarize a PDF:
1. Load the PDF using `PyPDFLoader`.
2. Split the document into chunks using `RecursiveCharacterTextSplitter`.
3. Apply the desired summarization chain.

## Output
The notebook provides outputs such as:
- Token counts for input text.
- Summaries in different languages.
- Final summaries with motivational titles.

## Notes
- Ensure your `GROQ_API_KEY` is valid and has sufficient permissions.
- Modify the templates and prompts to suit your specific use case.

## License
This project is licensed under the MIT License.
