import pandas as pd

data = {
    "Customer": ["A", "B", "C", "D"],
    "State": ["NY", "CA", "TX", "CA"],
    "Purchase_Amount": [500, 1500, 1200, 700]
}

df = pd.DataFrame(data)

# Filter customers from CA who made purchases over $1000
filtered_df = df[(df["State"] == "CA") & (df["Purchase_Amount"] > 1000)]
print(filtered_df)

