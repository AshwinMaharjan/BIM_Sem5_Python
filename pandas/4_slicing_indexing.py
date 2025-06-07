import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}

df = pd.DataFrame(data)

# slice rows from index 1 to 3
slice_rows = df.loc[1:3]

print("Sliced Rows:")
print(slice_rows)
print()

 # slicing columns from 'Name' to 'Age'
slice_columns = df.loc[:, 'Name':'Age']

print("Sliced Columns:")
print(slice_columns)


#name, city
data2=df.loc[1:3,['Name','Age']]
print(data2)