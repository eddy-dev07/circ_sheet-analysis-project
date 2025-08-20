import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("cricsheet.db")

# List of queries
queries = {
    "Top 10 team matchups in ODIs": """
        SELECT team1, team2, winner, COUNT(*) as matches
        FROM odis_matches
        GROUP BY team1, team2, winner
        ORDER BY matches DESC
        LIMIT 10;
    """,

    "Number of matches played by each team (ODIs)": """
        SELECT team1 AS team, COUNT(*) as matches
        FROM odis_matches
        GROUP BY team1
        UNION
        SELECT team2, COUNT(*)
        FROM odis_matches
        GROUP BY team2
        ORDER BY matches DESC;
    """,

    "Teams with highest win counts (ODIs)": """
        SELECT winner, COUNT(*) AS wins
        FROM odis_matches
        WHERE winner IS NOT NULL
        GROUP BY winner
        ORDER BY wins DESC
        LIMIT 10;
    """,

    "Toss decisions in Tests": """
        SELECT toss_decision, COUNT(*) AS times
        FROM tests_matches
        GROUP BY toss_decision
        ORDER BY times DESC;
    """,

    "Teams winning after winning toss (Tests)": """
        SELECT toss_winner, COUNT(*) AS wins_after_toss
        FROM tests_matches
        WHERE toss_winner = winner
        GROUP BY toss_winner
        ORDER BY wins_after_toss DESC;
    """,

    "Venues hosting most matches (ODIs)": """
        SELECT venue, COUNT(*) AS matches
        FROM odis_matches
        GROUP BY venue
        ORDER BY matches DESC
        LIMIT 10;
    """,

    "Venues hosting most matches (T20s)": """
        SELECT venue, COUNT(*) AS matches
        FROM t20s_matches
        GROUP BY venue
        ORDER BY matches DESC
        LIMIT 10;
    """,

    "Total matches per year (ODIs)": """
        SELECT SUBSTR(date, 1, 4) AS year, COUNT(*) AS matches
        FROM odis_matches
        GROUP BY year
        ORDER BY year;
    """,

    "Total matches per year (Tests)": """
        SELECT SUBSTR(date, 1, 4) AS year, COUNT(*) AS matches
        FROM tests_matches
        GROUP BY year
        ORDER BY year;
    """,

    "Teams with most losses (ODIs)": """
        SELECT team1 AS team, COUNT(*) AS losses
        FROM odis_matches
        WHERE winner != team1
        GROUP BY team1
        UNION
        SELECT team2, COUNT(*)
        FROM odis_matches
        WHERE winner != team2
        GROUP BY team2
        ORDER BY losses DESC;
    """,

    "Top 5 winners in T20s": """
        SELECT winner, COUNT(*) AS wins
        FROM t20s_matches
        WHERE winner IS NOT NULL
        GROUP BY winner
        ORDER BY wins DESC
        LIMIT 5;
    """,

    "Frequency of toss winners (ODIs)": """
        SELECT toss_winner, COUNT(*) AS times
        FROM odis_matches
        GROUP BY toss_winner
        ORDER BY times DESC;
    """,

    "Matches with no result (ODIs)": """
        SELECT COUNT(*) AS no_result_matches
        FROM odis_matches
        WHERE winner IS NULL;
    """,

    "Matches with no result (T20s)": """
        SELECT COUNT(*) AS no_result_matches
        FROM t20s_matches
        WHERE winner IS NULL;
    """,

    "Teams winning after losing toss (ODIs)": """
        SELECT team1, COUNT(*) AS wins_after_losing_toss
        FROM odis_matches
        WHERE toss_winner != winner AND winner = team1
        GROUP BY team1
        UNION
        SELECT team2, COUNT(*)
        FROM odis_matches
        WHERE toss_winner != winner AND winner = team2
        GROUP BY team2
        ORDER BY wins_after_losing_toss DESC;
    """,

    "Most common toss decision (ODIs)": """
        SELECT toss_decision, COUNT(*) AS times
        FROM odis_matches
        GROUP BY toss_decision
        ORDER BY times DESC;
    """,

    "Most common toss decision (T20s)": """
        SELECT toss_decision, COUNT(*) AS times
        FROM t20s_matches
        GROUP BY toss_decision
        ORDER BY times DESC;
    """,

    "Top winners in ODIs (proxy finals)": """
        SELECT winner, COUNT(*) AS titles
        FROM odis_matches
        GROUP BY winner
        ORDER BY titles DESC
        LIMIT 5;
    """,

    "Distribution of winners in Tests": """
        SELECT winner, COUNT(*) AS wins
        FROM tests_matches
        WHERE winner IS NOT NULL
        GROUP BY winner
        ORDER BY wins DESC
        LIMIT 10;
    """,

    "Toss decision vs. match wins (ODIs)": """
        SELECT toss_decision, COUNT(*) AS wins
        FROM odis_matches
        WHERE toss_winner = winner
        GROUP BY toss_decision;
    """
}

# Run queries and print results
with open("query_results.txt", "w", encoding="utf-8") as f:
    for title, q in queries.items():
        print(f"\n--- {title} ---")
        df = pd.read_sql(q, conn)
        print(df.head(20))  # show top 20 rows max
        f.write(f"\n--- {title} ---\n")
        f.write(df.to_string(index=False))
        f.write("\n")

conn.close()
print("\n All queries executed. Results saved to query_results.txt")
