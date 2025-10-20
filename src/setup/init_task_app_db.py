# Initializes a SQLite database with a 'tasks' table and sample data.

import sqlite3

DB_FILE = "task_app.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        description TEXT,
        status TEXT
    )
"""
)
cursor.executemany(
    "INSERT INTO tasks (description, status) VALUES (?, ?)",
    [("Task 1", "pending"), ("Task 2", "completed"), ("Task 3", "pending")],
)
conn.commit()
conn.close()

print("Database initialized with sample tasks.")
