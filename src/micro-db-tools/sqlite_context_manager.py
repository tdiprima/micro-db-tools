"""
Defines a context manager for simplified SQLite interactions, 
creates a table, inserts data, and retrieves it.
"""

import sqlite3


class SQLiteManager:
    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()


DB_FILE = "settings.db"


def perform_db_ops():
    with SQLiteManager(DB_FILE) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)")
        cursor.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?)",
            ("update_date", "2024-12-31"),
        )

    with SQLiteManager(DB_FILE) as cursor:
        cursor.execute("SELECT * FROM settings")
        print(f"Retrieved: {cursor.fetchone()}")


if __name__ == "__main__":
    perform_db_ops()
    # Retrieved: ('update_date', '2024-12-31')
