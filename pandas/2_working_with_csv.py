import pandas as pd

#reading the file without using to_string
data1=pd.read_csv('student_large.csv')
print(data1)

#reading the file by using to_string
data1=pd.read_csv('student_large.csv')
data2=data1.to_string() #display all the datas in one go
print(data2)