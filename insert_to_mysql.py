import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("traffic_stops_cleaned.csv")

# Create MySQL connection
engine = create_engine(
    "mysql+pymysql://root:Babirusa%402003@localhost/securecheck_db"
)

# Insert data into MySQL
df.to_sql(
    name="traffic_stops",
    con=engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully into MySQL")

