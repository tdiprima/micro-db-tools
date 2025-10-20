# Uses SQLAlchemy Core to define a table, insert data, and query active users programmatically without full ORM overhead.

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, select)

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()
user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("status", String),
)
metadata.create_all(engine)


def fetch_active_users():
    stmt = select(user_table).where(user_table.c.status == "active")
    with engine.connect() as connection:
        connection.execute(
            user_table.insert(),
            [
                {"name": "Eve", "status": "active"},
                {"name": "Frank", "status": "inactive"},
            ],
        )
        result = connection.execute(stmt)
        for row in result:
            print(f"Active User: {row.name}")


if __name__ == "__main__":
    fetch_active_users()
