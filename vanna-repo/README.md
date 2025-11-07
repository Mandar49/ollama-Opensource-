# AD AI MVP

This application provides a simple web server that allows you to ask questions about your ad campaign data in natural language.

## Running the Application (Windows)

Follow these three simple steps to get the application running:

### 1. Install the Required Packages

Open a command prompt and run the following command to install the necessary Python packages:

```
pip install -r requirements.txt
```

### 2. Train the AI

Next, run the training script to teach the AI about your database schema and business logic. This will create a `chroma.sqlite3` file in your project directory.

```
python train.py
```

### 3. Run the Web Server

Finally, start the Flask web server:

```
python ad_ai_app.py
```

You can now send questions to the `http://127.0.0.1:5000/api/ask` endpoint.
