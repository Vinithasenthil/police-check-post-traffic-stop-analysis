import pandas as pd

# Load Excel file
df = pd.read_excel("data/traffic_stops.xlsx")

# Check missing values BEFORE cleaning
print("Before cleaning:")
print(df.isnull().sum())

# Clean missing values
df['search_type'] = df['search_type'].fillna('No Search')

# Check AFTER cleaning
print("After cleaning:")
print(df['search_type'].isnull().sum())

# Save cleaned data
df.to_csv("traffic_stops_cleaned.csv", index=False)
print("Cleaned data saved succes" \
"sfully")

print(df.columns)
print(df.dtypes)

