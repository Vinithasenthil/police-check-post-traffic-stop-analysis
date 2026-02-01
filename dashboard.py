import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page config
st.set_page_config(page_title="SecureCheck Dashboard", layout="wide")

# Title
st.title("SecureCheck – Traffic Stops Analysis")

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:Babirusa%402003@localhost/securecheck_db"
)

# Load data
query = "SELECT * FROM traffic_stops"
df = pd.read_sql(query, engine)

# KPIs
st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total Arrests", int(df["is_arrested"].sum()))
col3.metric("Search Conducted", int(df["search_conducted"].sum()))

# Filters
st.subheader("Filter Data")
gender = st.selectbox(
    "Select Driver Gender",
    ["All"] + list(df["driver_gender"].dropna().unique())
)

if gender != "All":
    df = df[df["driver_gender"] == gender]

# Data preview
st.subheader("Traffic Stop Records")
st.dataframe(df.head(20))