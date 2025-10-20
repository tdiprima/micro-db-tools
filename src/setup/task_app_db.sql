-- Initializes a SQLite database with a 'tasks' table and sample data.
-- Run with: sqlite3 task_app.db < init_task_app_db.sql

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT,
    status TEXT
);

INSERT INTO tasks (description, status) VALUES ('Task 1', 'pending');
INSERT INTO tasks (description, status) VALUES ('Task 2', 'completed');
INSERT INTO tasks (description, status) VALUES ('Task 3', 'pending');
