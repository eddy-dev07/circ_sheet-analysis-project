import os
import json
import sqlite3
import pandas as pd

# Define folder paths (adjust case sensitivity for your folders)
folders = {
    "tests": "Data/TESTs",
    "odis": "Data/ODIs",
    "t20s": "Data/T20s"
}

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect("cricsheet.db")

def load_json_files(folder):
    """Load all JSON files from a folder into a DataFrame"""
    data = []
    for file in os.listdir(folder):
        if file.endswith(".json"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                match = json.load(f)
                # Extract metadata
                row = {
                    "match_id": file.replace(".json",""),
                    "date": match.get("info", {}).get("dates", [None])[0],
                    "venue": match.get("info", {}).get("venue"),
                    "team1": match.get("info", {}).get("teams", [None,None])[0],
                    "team2": match.get("info", {}).get("teams", [None,None])[1],
                    "winner": match.get("info", {}).get("outcome", {}).get("winner"),
                    "toss_winner": match.get("info", {}).get("toss", {}).get("winner"),
                    "toss_decision": match.get("info", {}).get("toss", {}).get("decision")
                }
                data.append(row)
    return pd.DataFrame(data)

# Loop through formats
for match_type, folder in folders.items():
    df = load_json_files(folder)
    print(f"{match_type} loaded: {len(df)} matches")
    # Save into SQLite
    df.to_sql(f"{match_type}_matches", conn, if_exists="replace", index=False)

conn.close()
print("✅ All data saved to cricsheet.db")
