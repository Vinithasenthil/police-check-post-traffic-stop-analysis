# Police Check Post Traffic Stop Analysis System

## Overview
This project implements an end-to-end traffic stop analysis system for police check post operations. It focuses on cleaning traffic stop data, storing it in a MySQL database, analyzing it using SQL queries, and visualizing insights through a Streamlit dashboard.

The project is implementation-focused and created for placement evaluation.

## Technologies Used
- Python
- Pandas
- MySQL
- SQL
- Streamlit

## Project Structure
- `dashboard.py` – Streamlit dashboard (main entry file)
- `preprocessing.py` – Data cleaning and preprocessing
- `insert_to_mysql.py` – Inserts cleaned data into MySQL
- `sql/` – SQL scripts for table creation and analysis
- `results.md` – Observations from SQL analysis
- `project_overview/` – Detailed project flow

## How to Run
python -m streamlit run dashboard.py --server.port 8502


## Outcome
The project identifies repeat vehicle stops, frequently searched vehicles, and arrest patterns. These insights support data-driven decision-making and improve the efficiency of police check post monitoring.
