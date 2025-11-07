# AD AI: Your Personal Data Analyst

AD AI is a powerful, yet simple, application that allows you to have a conversation with your advertising data. Powered by a "Two-Brain" AI architecture, it can answer both factual, data-driven questions and provide high-level strategic advice.

This MVP (Minimum Viable Product) is designed to be lean, easy to run, and highly customizable. It uses Vanna.AI to connect to your database, Ollama to run the `gemma:7b` language model locally, and a Flask-based web server to provide an API for your questions.

## Features

- **"Two-Brain" Architecture**: AD AI automatically routes your questions to the best "brain" for the job:
    - **The Factual Brain**: For questions about specific numbers and data (e.g., "What was our total spend last month?"). This brain uses Vanna to generate and run SQL queries, ensuring you get accurate, data-backed answers.
    - **The Strategic Brain**: For more open-ended questions (e.g., "How can we improve our ad performance?"). This brain uses a general-purpose language model to provide creative, strategic insights.
- **Natural Language Summaries**: The "Presentation Layer" transforms raw data into friendly, easy-to-understand sentences.
- **Local First**: Your data and the AI model run entirely on your local machine, ensuring privacy and security.
- **Easy to Customize**: The training script (`train.py`) can be easily updated with your own database schema, business logic, and common questions.

## Getting Started (for Windows)

Follow these simple steps to get your AD AI up and running.

### Prerequisites

- Python 3.8+ installed on your system.
- An instance of MySQL with the `ad_ai_testdb` database created.
- Ollama installed and the `gemma:7b` model pulled (`ollama pull gemma:7b`).

### 1. Install Dependencies

Open a command prompt and navigate to your project directory. Then, run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Configure Your Database

Before you can train the AI, you need to tell it how to connect to your database.

- Open the `common.py` file in a text editor.
- Locate the `db_config` dictionary.
- Replace the placeholder values for `host`, `user`, `password`, and `database` with your actual MySQL credentials.

```python
# In common.py
db_config = {
    'host': 'your_mysql_host',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'ad_ai_testdb'
}
```

### 3. Train the AI

Now, it's time to teach the AI about your data. The training script will create a local `chroma.sqlite3` file, which is the AI's "memory."

Run the training script from your command prompt:

```bash
python train.py
```

*For more information on how to customize the training, see the "Custom Training" section below.*

### 4. Run the Application

Finally, start the Flask web server:

```bash
python ad_ai_app.py
```

Your AD AI is now running! The API is available at `http://127.0.0.1:5000/api/ask`.

## Custom Training

The `train.py` file is where you teach the AI about your specific data. You can improve its accuracy and capabilities by adding more information in three key areas (the "Three Pillars"):

1.  **DDL**: Add the `CREATE TABLE` statements for your database schema. This helps the AI understand the structure of your data.
2.  **Documentation**: Add plain-English descriptions of your business logic and terminology.
3.  **Question-SQL Pairs**: Provide examples of complex questions and the exact SQL queries that answer them. This is the most effective way to train the AI on your specific use cases.

## API Usage

You can interact with your AD AI by sending a `POST` request to the `/api/ask` endpoint.

Here is an example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"question\": \"What is the total spend for the 'Summer Sale' campaign?\"}" http://127.0.0.1:5000/api/ask
```

You will receive a JSON response containing the answer.
