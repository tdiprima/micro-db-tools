# Connects to a SQLite database and fetches active users as a list of dictionaries, printing their details without manual cursor handling.

import records

DB_URL = "sqlite:///user_data.db"


def fetch_active_users():
    db = records.Database(DB_URL)
    rows = db.query("SELECT name, email FROM users WHERE is_active=true")
    for row in rows:
        row_dict = row.as_dict()
        print(f"User: {row_dict['name']}, Email: {row_dict['email']}")


if __name__ == "__main__":
    fetch_active_users()
