
import csv

# Reading specific columns from emp.csv
with open("emp.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[1], row[3])
