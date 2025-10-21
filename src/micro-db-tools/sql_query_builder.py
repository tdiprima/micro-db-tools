"""
Builds a complex SQL query programmatically using Python objects and 
prints the generated SQL string.
"""

from pypika import Query, Table


def generate_sql_query():
    sales = Table("sales")
    clients = Table("clients")

    q = (
        Query.from_(sales)
        .select(sales.id, clients.name, sales.total)
        .join(clients)
        .on(sales.client_id == clients.id)
        .where(sales.total > 200)
        .orderby(sales.total, ascending=False)
    )

    print(q.get_sql(quote_char=None))


if __name__ == "__main__":
    generate_sql_query()
    # SELECT sales.id,clients.name,sales.total FROM sales JOIN clients ON sales.client_id=clients.id WHERE sales.total>200 ORDER BY sales.total
