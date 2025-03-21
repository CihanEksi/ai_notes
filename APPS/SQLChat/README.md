# SQL Chat

SQL Chat is a Streamlit-based application that allows users to interact with SQL databases using natural language queries. It leverages the power of the GROQ language model to provide intelligent responses and insights.

## Features

- **Database Connectivity**: Connect to a local SQLite database or a remote MySQL database.
- **Natural Language Queries**: Ask questions in plain English, and the app translates them into SQL queries.
- **Interactive Chat Interface**: Chat-based interface for seamless interaction.
- **Error Handling**: Handles parsing errors gracefully for a smooth user experience.

## Requirements

- Python 3.8 or higher
- Streamlit
- GROQ API Key
- MySQL (optional, if connecting to a MySQL database)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SQLChat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the SQLite database:
   - Ensure the `employees.db` file is present in the application directory.

4. (Optional) Set up a MySQL database:
   - Ensure you have a running MySQL instance and provide the connection details in the app.

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Select the database type:
   - **Use SQL3 Database**: Connect to the local SQLite database.
   - **Connect to your Database**: Provide MySQL connection details.

4. Enter your GROQ API Key in the sidebar.

5. Start asking questions in the chat interface.

## Notes

- Ensure you have a valid GROQ API Key to use the application.
- For MySQL, provide the host, user, password, and database name in the sidebar.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [Streamlit](https://streamlit.io/)
- [GROQ](https://groq.com/)
