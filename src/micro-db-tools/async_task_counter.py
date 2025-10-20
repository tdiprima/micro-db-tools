# Uses asynchronous SQLite to count and print the number of pending tasks without blocking the event loop.

import asyncio

import aiosqlite

DB_NAME = "task_app.db"


async def count_pending_tasks():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            'SELECT count(*) FROM tasks WHERE status="pending"'
        ) as cursor:
            row = await cursor.fetchone()
            print(f"Pending tasks: {row[0]}")


if __name__ == "__main__":
    asyncio.run(count_pending_tasks())
