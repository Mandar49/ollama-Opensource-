import pandas as pd
import mysql.connector
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        # Vanna requires a path for the vector store, and a model for the LLM
        ChromaDB_VectorStore.__init__(self, config={'path': 'chroma.sqlite3'})
        Ollama.__init__(self, config={'model': 'gemma:7b'})

    def run_sql(self, sql: str) -> pd.DataFrame:
        """
        Run a SQL query against the ad_ai_testdb database.
        """
        # Replace with your actual database configuration
        db_config = {
            'host': 'localhost',
            'user': 'user',
            'password': 'password',
            'database': 'ad_ai_testdb'
        }

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(sql)

            # Fetch column names from cursor description
            column_names = [desc[0] for desc in cursor.description]

            # Fetch all rows
            rows = cursor.fetchall()

            df = pd.DataFrame(rows, columns=column_names)
            return df

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return pd.DataFrame() # Return an empty DataFrame on error

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

# Instantiate the Vanna agent. This will be imported by other scripts.
vn = MyVanna()
