import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

st.set_page_config(page_title="SecureCheck Dashboard", layout="wide")

st.title("SecureCheck – Traffic Stops Analysis")
st.markdown(
    "A Python–SQL based dashboard for analyzing police traffic stop records "
    "and generating real-time insights."
)

engine = create_engine(
    "mysql+pymysql://root:Babirusa%402003@localhost/securecheck_v2"
)



# KPIs
st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)

total_records = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_stops", engine
)["total"][0]

total_arrests = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_stops WHERE is_arrested = 1", engine
)["total"][0]

total_searches = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_stops WHERE search_conducted = 1", engine
)["total"][0]

col1.metric("Total Records", total_records)
col2.metric("Total Arrests", total_arrests)
col3.metric("Search Conducted", total_searches)

# Filter
st.subheader("Filter Data")
gender = st.selectbox("Select Driver Gender", ["All", "Male", "Female"])

query = "SELECT * FROM traffic_stops"
params = {}

if gender != "All":
    query += " WHERE driver_gender = :gender"
    params["gender"] = gender

query += " LIMIT 50"

filtered_df = pd.read_sql(text(query), engine, params=params)

# Advanced Insights
st.subheader("Advanced Insights (SQL)")
query_option = st.selectbox(
    "Select a Query to Run",
    [
        "Top 5 Most Frequent Search Types",
        "Stops by Hour of Day",
        "Arrest Rate by Country"
    ]
)

if st.button("Run Query"):
    if query_option == "Top 5 Most Frequent Search Types":
        sql_query = """
        SELECT search_type, COUNT(*) AS count
        FROM traffic_stops
        GROUP BY search_type
        ORDER BY count DESC
        LIMIT 5;
        """
    elif query_option == "Stops by Hour of Day":
        sql_query = """
        SELECT HOUR(stop_time) AS hour, COUNT(*) AS stops
        FROM traffic_stops
        GROUP BY hour
        ORDER BY hour;
        """
    elif query_option == "Arrest Rate by Country":
        sql_query = """
        SELECT country_name,
               COUNT(*) AS total_stops,
               SUM(is_arrested) AS arrests,
               ROUND(SUM(is_arrested)/COUNT(*)*100, 2) AS arrest_rate
        FROM traffic_stops
        GROUP BY country_name;
        """

    result = pd.read_sql(sql_query, engine)
    st.dataframe(result)

# Rule-based prediction
st.subheader("Add New Police Log & Predict Outcome")

with st.form("prediction_form"):
    stop_date = st.date_input("Stop Date")
    stop_time = st.time_input("Stop Time")
    vehicle_number = st.text_input("Vehicle Number")
    driver_age = st.number_input("Driver Age", min_value=18, max_value=100)
    driver_gender = st.selectbox("Driver Gender", ["Male", "Female"])
    country = st.selectbox("Country", ["India", "USA", "Canada"])
    violation = st.text_input("Violation")
    search_conducted = st.selectbox("Search Conducted", [0, 1])
    submitted = st.form_submit_button("Predict Outcome")

if submitted:
    prediction = "Arrest" if violation.upper() == "DUI" else "Citation / Warning"
    st.success(f"Predicted Stop Outcome: {prediction}")

with st.expander("View Traffic Stop Records"):
    st.dataframe(filtered_df.head(50))
