import sqlite3, pandas as pd

# connect to your database
conn = sqlite3.connect("cricsheet.db")

# tables and formats
tables = {"ODI": "odis_matches", "Test": "tests_matches", "T20": "t20s_matches"}
dfs = []

# export each table as CSV
for fmt, tbl in tables.items():
    df = pd.read_sql(f"SELECT * FROM {tbl}", conn)
    df["format"] = fmt
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    dfs.append(df)
    df.to_csv(f"matches_{fmt.lower()}.csv", index=False)

conn.close()

# combine all into one CSV
all_df = pd.concat(dfs, ignore_index=True)
all_df.to_csv("matches_all.csv", index=False)

print(" Saved: matches_all.csv + matches_odi.csv + matches_test.csv + matches_t20.csv")
