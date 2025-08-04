import pandas as pd
import sqlite3
import os

# Load the CSV
csv_path = os.path.join("data", "sales_data.csv")
df = pd.read_csv(csv_path)

# Connect to SQLite DB
db_path = os.path.join("db", "sales.db")
conn = sqlite3.connect(db_path)

# Save data to DB
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data loaded into SQLite database successfully.")

conn.close()
