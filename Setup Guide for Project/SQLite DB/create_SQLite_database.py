import sqlite3
import os

# Define the path to the SQLite database
db_dir = "C:\Users\dylan\Dropbox\MyMASProject\4MAS-MemGPT_MetGPT_ChatDev_AutoGPT\agents\newproject\MemGPT\archival DB storage\SQLite"
db_file = os.path.join(db_dir, "SQLite_memgpt_docs.db")

# Ensure directory exists
os.makedirs(db_dir, exist_ok=True)

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table for document embeddings
cursor.execute('''
CREATE TABLE sqlite_docs_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    embedding BLOB
);
''')
conn.commit()
conn.close()
