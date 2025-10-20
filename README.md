# 🐍 Python Micro DB Tools

![Personal Repo](https://img.shields.io/badge/🔒-personal_repo-blueviolet?style=for-the-badge)

Welcome to the chill zone of Python database stuff.  
This repo's all about **tiny but mighty** DB helpers — no bloated ORMs, just pure vibes and clean queries.  
Each script shows a simple, low-key way to do SQL, async ops, and data stuff without 500 lines of setup.

## ⚙️ What's Inside

* `fetch_active_users.py` → grabs users with `records` (easy mode)
* `instant_data_storage.py` → instant storage using `dataset` (plug & play fr)
* `async_task_counter.py` → async DB reads with `aiosqlite` (✨ async supremacy ✨)
* `core_active_users.py` → runs queries with SQLAlchemy Core (no ORM drama)
* `sql_query_builder.py` → builds SQL strings using `pypika` (SQL but make it Lego)
* `sqlite_context_manager.py` → SQLite ops made brain-dead simple
* `peewee_blog_manager.py` → tiny ORM magic with Peewee (cute but powerful)

## 🚀 Setup

1. Install deps like a pro:

   ```bash
   uv add records dataset aiosqlite sqlalchemy pypika peewee
   ```
2. (Optional) Set up sample DBs for demos:

   ```bash
   python init_user_data_db.py
   ```
3. Run your script of choice:

   ```bash
   python <script_name>.py
   ```

## 💡 Why This Exists

Cuz sometimes you just wanna **talk to a database** without wrestling a whole framework for it.  
These little scripts keep it minimal, readable, and actually fun to use.
