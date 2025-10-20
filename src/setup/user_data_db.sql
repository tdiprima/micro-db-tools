-- Initializes a SQLite database with a 'users' table and sample data.
-- Run with: sqlite3 user_data.db < user_data_db.sql

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    is_active BOOLEAN
);

INSERT INTO users (name, email, is_active) VALUES ('Alice', 'alice@example.com', 1);
INSERT INTO users (name, email, is_active) VALUES ('Bob', 'bob@example.com', 0);
INSERT INTO users (name, email, is_active) VALUES ('Charlie', 'charlie@example.com', 1);
