import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to DB
conn = sqlite3.connect("cricsheet.db")

# Load data
odis = pd.read_sql("SELECT * FROM odis_matches", conn)
tests = pd.read_sql("SELECT * FROM tests_matches", conn)
t20s = pd.read_sql("SELECT * FROM t20s_matches", conn)

conn.close()

print("ODIs:", odis.shape)
print("Tests:", tests.shape)
print("T20s:", t20s.shape)

# -------------------------------
# 1. ODI Matches per Year
odis['year'] = odis['date'].str[:4]
plt.figure(figsize=(10,5))
sns.countplot(data=odis, x='year', order=odis['year'].value_counts().index)
plt.title("ODI Matches per Year")
plt.xticks(rotation=90)
plt.savefig("odi_matches_per_year.png")
plt.close()

# -------------------------------
# 2. Top 10 ODI Venues
plt.figure(figsize=(10,5))
odis['venue'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Venues for ODIs")
plt.savefig("odi_top_venues.png")
plt.close()

# -------------------------------
# 3. Top 10 ODI Winning Teams
plt.figure(figsize=(10,5))
odis['winner'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Winning Teams in ODIs")
plt.savefig("odi_top_winners.png")
plt.close()

# -------------------------------
# 4. Toss Decision Counts (ODIs)
plt.figure(figsize=(6,4))
sns.countplot(data=odis, x='toss_decision')
plt.title("ODI Toss Decisions (Bat/Field)")
plt.savefig("odi_toss_decisions.png")
plt.close()

# -------------------------------
# 5. Toss Winner vs Match Winner (ODIs)
odis['toss_match_win'] = (odis['toss_winner'] == odis['winner'])
odis['toss_match_win'].value_counts().plot(kind='bar')
plt.title("Toss Winner Also Won Match? (ODIs)")
plt.xticks([0,1], ["No","Yes"])
plt.savefig("odi_toss_vs_match.png")
plt.close()

# -------------------------------
# 6. Test Matches per Year
tests['year'] = tests['date'].str[:4]
plt.figure(figsize=(10,5))
sns.countplot(data=tests, x='year', order=tests['year'].value_counts().index)
plt.title("Test Matches per Year")
plt.xticks(rotation=90)
plt.savefig("test_matches_per_year.png")
plt.close()

# -------------------------------
# 7. Top 10 Test Venues
plt.figure(figsize=(10,5))
tests['venue'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Venues for Tests")
plt.savefig("test_top_venues.png")
plt.close()

# -------------------------------
# 8. T20 Matches per Year
t20s['year'] = t20s['date'].str[:4]
plt.figure(figsize=(10,5))
sns.countplot(data=t20s, x='year', order=t20s['year'].value_counts().index)
plt.title("T20 Matches per Year")
plt.xticks(rotation=90)
plt.savefig("t20_matches_per_year.png")
plt.close()

# -------------------------------
# 9. Top 10 T20 Winning Teams
plt.figure(figsize=(10,5))
t20s['winner'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Winning Teams in T20s")
plt.savefig("t20_top_winners.png")
plt.close()

# -------------------------------
# 10. Compare Total Matches Across Formats
match_counts = [len(odis), len(tests), len(t20s)]
formats = ["ODI","Test","T20"]

plt.bar(formats, match_counts)
plt.title("Total Matches by Format")
plt.savefig("format_match_comparison.png")
plt.close()

print(" All 10 graphs generated and saved as PNGs.")
