
import csv

# Extracting columns 1, 2, and 3 into a list of tuples
data = []
with open("emp.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append((row[1], row[2], row[3]))

print(data)
