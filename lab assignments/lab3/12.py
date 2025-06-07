import pandas as pd

df = pd.read_csv("data.csv")  # Load CSV file

df.fillna(0, inplace=True)  # Replace NaN with 0
df.dropna(inplace=True)  # Drop rows with missing values
print(df)

