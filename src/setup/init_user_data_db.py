# Initializes a SQLite database with a 'users' table and sample data.

import sqlite3

DB_FILE = "user_data.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        is_active BOOLEAN
    )
"""
)
cursor.executemany(
    "INSERT INTO users (name, email, is_active) VALUES (?, ?, ?)",
    [
        ("Alice", "alice@example.com", True),
        ("Bob", "bob@example.com", False),
        ("Charlie", "charlie@example.com", True),
    ],
)
conn.commit()
conn.close()

print("Database initialized with sample users.")
