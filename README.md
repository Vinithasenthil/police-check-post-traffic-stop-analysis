

# SECURE CHECK – ETL Based Police Check Post Traffic Stop Analysis System

## Overview
This project implements an end-to-end traffic stop analysis system for police check post operations.  
It focuses on cleaning raw traffic stop data, storing it in a MySQL database, analyzing it using SQL queries, and visualizing insights through an interactive Streamlit dashboard.

When the dashboard is run, it **opens automatically in the web browser** and displays real-time insights from the MySQL database.

---

## ETL Process

### Extract
- Raw traffic stop data is collected from structured source files (`traffic_stops.xlsx`).
- Data is extracted into Python using Pandas for processing.

### Transform
- Data cleaning and preprocessing are performed using Pandas:
  - Handling missing and null values  
  - Standardizing data types and formats  
  - Removing invalid or inconsistent records  
- The transformed data is saved as a clean CSV file (`traffic_stops_cleaned.csv`).

### Load
- The cleaned dataset is loaded into a **MySQL database**.
- Data is inserted into a structured table (`traffic_stops`) for analytics.
- SQL queries are used to validate the loaded data.

---

## Technologies Used
- Python  
- Pandas  
- MySQL  
- SQL  
- Streamlit  

---

## Project Structure

- **dashboard.py**  
  Main Streamlit application.  
  Connects to MySQL, calculates KPIs, applies filters, and displays SQL-based insights.  
  The dashboard opens in the browser on port `8502`.

- **preprocessing.py**  
  Cleans and preprocesses raw traffic stop data (handling null values, data types, and formatting).

- **insert_to_mysql.py**  
  Loads the cleaned dataset into the MySQL database table (`traffic_stops`).

- **data/**  
  Contains raw and cleaned datasets:
  - `traffic_stops.xlsx`
  - `traffic_stops_cleaned.csv`

- **sql/**  
  Contains SQL queries used for analysis and insights.

- **results.md**  
  Documents key observations derived from SQL analysis.

- **project_overview**  
  Explains the complete project workflow and logic.

---

## Dashboard Features

### Key Performance Indicators (KPIs)
- Total Records  
- Total Arrests  
- Search Conducted Count  

These KPIs are calculated directly from the MySQL database and update dynamically.

---

### Filters in Streamlit Dashboard
- **Driver Gender Filter**  
  Allows users to filter all dashboard metrics and insights based on driver gender (All, Male, Female).

The filter updates:
- KPI values  
- SQL insight results  
- Tables displayed in the dashboard  

---

### Advanced Insights (SQL)
Users can interactively select and run predefined SQL queries:

- Arrest Rate by Country  
- Top 5 Most Frequent Search Types  
- Stops by Hour of Day  

Results are displayed instantly in tabular form.

---

## How to Run the Dashboard


python -m streamlit run dashboard.py --server.port 8502

After running the command

## The Streamlit dashboard opens automatically in the browser

URL: http://localhost:8502

## Project Documentation

https://github.com/Vinithasenthil/police-check-post-traffic-stop-analysis/blob/main/streamlit%20dashboard.pdf




