import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]})

# Boolean Indexing: Select rows where A > 2
filtered_df = df[df["A"] > 2]

# Fancy Indexing: Select specific rows
selected_rows = df.iloc[[0, 2]]

print("Boolean Indexing:\n", filtered_df)
print("Fancy Indexing:\n", selected_rows)

