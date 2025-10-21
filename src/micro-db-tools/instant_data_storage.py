"""
A quick data storage utility using dataset for rapid prototyping.
Connects to a SQLite database and inserts data into an auto-created table, 
then retrieves and prints a specific record.
"""
import dataset

DB_URL = "sqlite:///quick_data.db"


def store_data_quickly(key, count):
    db = dataset.connect(DB_URL)
    metrics_table = db["metrics"]
    metrics_table.insert({"key": key, "count": count, "is_active": True})
    record = metrics_table.find_one(key=key)
    if record:
        print(f"Found record: {record}")


if __name__ == "__main__":
    store_data_quickly("login_metrics", 500)
    store_data_quickly("error_metrics", 120)

# Found record: OrderedDict([('id', 1), ('key', 'login_metrics'), ('count', 500), ('is_active', True)])
# Found record: OrderedDict([('id', 2), ('key', 'error_metrics'), ('count', 120), ('is_active', True)])
