import sqlite3
import pandas as pd

# Connect to your DB
conn = sqlite3.connect("cricsheet.db")

# Show tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in DB:\n", tables)

# Preview some rows from Tests
df = pd.read_sql("SELECT * FROM tests_matches LIMIT 5;", conn)
print("\nSample rows from Tests table:\n", df)

# Preview some rows from ODIs
df = pd.read_sql("SELECT * FROM odis_matches LIMIT 5;", conn)
print("\nSample rows from ODIs table:\n", df)

# Preview some rows from T20s
df = pd.read_sql("SELECT * FROM t20s_matches LIMIT 5;", conn)
print("\nSample rows from T20s table:\n", df)

conn.close()
