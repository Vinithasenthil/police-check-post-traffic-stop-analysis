import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("data/traffic_stops_cleaned.csv")
df = df.drop(columns=["stop_id"], errors="ignore")

# Create MySQL connection
engine = create_engine(
    "mysql+pymysql://root:Babirusa%402003@localhost/securecheck_v2"
)


# Insert data into MySQL
df.to_sql(
    name="traffic_stops",
    con=engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully into MySQL")


