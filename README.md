# 🏏 CricSheet Match Analysis Project

## 📌 Project Overview
This project analyzes cricket match data (ODIs, Tests, and T20s) using the CricSheet dataset. It demonstrates the full data pipeline:
- Extracting raw JSON files  
- Loading into an SQLite database  
- Running SQL queries for insights  
- Performing Exploratory Data Analysis (EDA) in Python  
- Creating an interactive Power BI Dashboard for visualization  

## ⚙️ Project Workflow
### 1️⃣ Data Pipeline
- Script: `pipeline.py`  
- Reads JSON data for ODIs, Tests, and T20s.  
- Extracts match metadata: date, venue, teams, winner, toss decision.  
- Loads data into SQLite database (`cricsheet.db`).  

### 2️⃣ Export for Power BI
- Script: `export_for_powerbi.py`  
- Reads database tables.  
- Adds format and year columns.  
- Exports CSVs: `matches_odi.csv`, `matches_test.csv`, `matches_t20.csv`, and combined `matches_all.csv`.  

### 3️⃣ Exploratory Data Analysis (EDA)
- Script: `eda.py`  
- Generates 10 insights/plots including:  
  - Matches per year (ODIs, Tests, T20s)  
  - Top venues by format  
  - Top winning teams  
  - Toss decision trends  
  - Toss winner vs match winner analysis  
  - Format comparison  

### 4️⃣ SQL Insights
- Script: `run_queries.py`  
- Runs multiple queries (Top matchups, Wins after toss, Matches per venue, etc.)  
- Results stored in `query_results.txt`.  

### 5️⃣ Power BI Dashboard
- File: `cricsheet_dashboard.pbix`  
- Interactive visuals created:  
  - ✅ KPI Cards: Total Matches, Teams, Venues  
  - ✅ Trend of Matches per Year  
  - ✅ Matches Won by Teams (Total + Across Formats)  
  - ✅ Distribution of Matches by Format  
  - ✅ Toss Decisions (Bat vs Field)  
  - ✅ Win % Share by Teams  

## 📂 Repository Structure
CRICKSHEET_PROJECT/
│── Data/ # Raw JSON data (ODIs, Tests, T20s)
│── cricsheet.db # SQLite database
│── pipeline.py # Ingest JSON → SQLite
│── export_for_powerbi.py # Export tables → CSVs for Power BI
│── eda.py # Exploratory Data Analysis (10 plots)
│── run_queries.py # SQL queries for insights
│── query_results.txt # SQL query outputs
│── matches_all.csv # Combined dataset for BI
│── *.png # Visualization outputs
│── *.csv # Individual format exports
│── *.pbix # Power BI dashboard file
│── README.md # Project documentation

## 🛠️ Tech Stack
- Python → Data processing, EDA  
- SQLite → Database  
- Pandas, Matplotlib, Seaborn → Analysis & visualization  
- SQL → Analytical queries  
- Power BI → Dashboard & storytelling  

## 📌 Key Insights
- 📈 Matches have grown sharply since 2010, especially T20s.  
- 🏆 Australia, India, and England dominate across formats.  
- 🏟️ Over 574 unique venues have hosted matches.  
- 🎲 Toss choice doesn’t guarantee victory — outcomes vary by format.  
- 🌍 Dataset includes not just ICC full members but also associates and special teams (103 distinct winners).  

## Install dependencies
pip install pandas matplotlib seaborn
## Run the pipeline
python pipeline.py
## Export CSVs for Power BI
python export_for_powerbi.py
## Run EDA
python eda.py
## Explore queries
python run_queries.py
## Credits
Dataset: CricSheet
Project Author: Aaditya (eddy-dev07)
