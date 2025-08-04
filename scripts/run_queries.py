import sqlite3
import os

# Get absolute path to db
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "db", "sales.db")
conn = sqlite3.connect(db_path)

# Read the queries.sql file
queries_file = os.path.join(base_dir, "scripts", "queries.sql")
with open(queries_file, "r") as f:
    sql_script = f.read()

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

# Execute each query
for i, query in enumerate(queries, start=1):
    print(f"\n--- Query {i} ---")
    cursor = conn.execute(query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    print(columns)
    for row in rows:
        print(row)

conn.close()
print("\n✅ All queries executed.")
