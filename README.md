 Project 1: Sales Data Insights Pipeline

1.Project Objective
To build a simple data pipeline using Python, SQLite, and CSV files to:
•	Load sales data into a database
•	Execute analysis queries
•	Display insights
This shows a basic data engineering workflow.
________________________________________
2️. Project Folder Structure
Folder Organization:
sales_pipeline/
├── data/        # Contains raw data files
│   └── sales_data.csv
├── db/          # Contains the SQLite database
│   └── sales.db
├── scripts/     # Python and SQL scripts
│   ├── load_data.py
│   └── run_queries.py
│   └── queries.sql
└── README.md
Purpose:
•	Keeps everything organized.
•	Makes the pipeline easy to maintain.
________________________________________
3️.Data Preparation
File: data/sales_data.csv
Description:
A CSV file containing sample sales records, e.g.:
OrderID,Product,Category,Sales,Region,OrderDate
1001,Laptop,Electronics,1200,North,2023-01-10
1002,Mobile,Electronics,800,South,2023-01-15
1003,Book,Stationery,20,North,2023-01-12
1004,Pen,Stationery,5,East,2023-01-11
1005,Tablet,Electronics,600,West,2023-01-18
Purpose:
This is the input dataset to be loaded into the database.
________________________________________
4️.Loading Data into SQLite
Script: scripts/load_data.py
What it does:
•	Imports required libraries (pandas, sqlite3, os)
•	Reads the CSV file into a pandas DataFrame
•	Connects to an SQLite database (sales.db)
•	Writes the data into a table called sales
Code:
import pandas as pd #This imports the pandas library and gives it the alias pd.
#We use pandas to read the CSV file and work with it like a table
import sqlite3 #It connects to and create the sales.db file, and write data into it.
import os # It help build file paths

# Load the CSV- It builds the path to the CSV file: Like : data/sales_data.csv
csv_path = os.path.join("data", "sales_data.csv")
df = pd.read_csv(csv_path) #df:DataFrame, It reads the CSV file

# Connect to SQLite DB- db:database, same as CVS_path. Creates the path for db like: db/sales.db
db_path = os.path.join("db", "sales.db")
conn = sqlite3.connect(db_path) # conn is connection, here we are connecting sqlite db.

# Here we created a new table as sales, used replace if any table exists in db. Index as false: we do not want pandas to create row index
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data loaded into SQLite database successfully.")

conn.close() # the connection is closed

Output:
✅ Prints confirmation:
✅ Data loaded into SQLite database successfully.
Effect:
•	Creates or updates sales.db with a fresh sales table.
________________________________________
5️. Writing SQL Queries
File: scripts/queries.sql
Example Queries:
-- Show all records
SELECT * FROM sales;
-- Total sales by region
SELECT Region, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region;

-- Top 3 highest sales transactions
SELECT * FROM sales
ORDER BY Sales DESC
LIMIT 3;

-- Total sales by product category
SELECT Category, SUM(Sales) AS CategorySales
FROM sales
GROUP BY Category;

Purpose:
These queries analyze the sales data.
________________________________________
6️. Running the Queries
Script: scripts/run_queries.py
Key Code:
import sqlite3 # it loads sqlite lib and connects to db
import os # used to creat file paths

“”” Get absolute path to db( why did I use absolute path here is there was an error at 1st used relative path (db_path = os.path.join("..", "db", "sales.db")which popped an error saying as “unable to open db file”. Hence, googled and check for alternative, it gave the absolute path version to avoid this error”””
# I understood using absolute path we can run the code in any terminal : which creates the full path
# Get the absolute path to the project root folder
# __file__ = path to this Python file (run_queries.py)
# os.path.abspath(__file__) = full path to this file
# os.path.dirname() = go up one folder (from scripts/)
# another os.path.dirname() = go up again to reach project root (sales_pipeline/)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# create full path to the database file: db/sales.db
db_path = os.path.join(base_dir, "db", "sales.db")
conn = sqlite3.connect(db_path) # connecting to db

# create full path to the SQL file: scripts/queries.sql
queries_file = os.path.join(base_dir, "scripts", "queries.sql")
with open(queries_file, "r") as f:
    sql_script = f.read()
# Splits the entire SQL text into separate queries wherever a semicolon (;) is found
# q.strip()
Removes any extra spaces
# if q.strip()
Ensures that only non-empty queries are included
queries = [q.strip() for q in sql_script.split(";") if q.strip()]

“”” Used Loop to execute each query one by one: queries is a list of SQL statements.
enumerate() is a function, it creates index(position). start=1 means the numbering will begin at 1”””
for i, query in enumerate(queries, start=1): # I is the query number as 1,2,3
    print(f"\n--- Query {i} ---")
    cursor = conn.execute(query)
# Get column names from the result    
columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    print(columns)
    for row in rows:
        print(row)
# Close the database connection
conn.close()
print("\n✅ All queries executed.")

Output:
✅ Prints each query’s results, e.g.:
--- Query 1 ---
['OrderID', 'Product', 'Category', 'Sales', 'Region', 'OrderDate']
(1001, 'Laptop', 'Electronics', 1200, 'North', '2023-01-10')

--- Query 2 ---
['Category', 'CategorySales']
('Electronics', 2600)
('Stationery', 25)
Effect:
Shows all records and aggregates as designed.
________________________________________
7️.End Result
Outcome:
•	Data pipeline automatically loads CSV data into SQLite.
•	All queries run in sequence and produce readable outputs.


✅ Project Completed Successfully
