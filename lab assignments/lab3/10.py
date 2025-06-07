import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [60000, 55000, 50000, 52000]
}

df = pd.DataFrame(data)
df.set_index(["Department", "Employee"], inplace=True)
print(df)

