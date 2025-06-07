import pandas as pd

data=pd.read_csv('employee.csv',index_col=0)
# print(data.to_string())

#adding columns
data['Age']=[50,60,70,80,90]
# print(data)

#adding same value for all columns
data['shift']='Morning'
# print(data)

#adding rows in the table
data.loc['E106',:]=["Gita","Manager",7000,800,80,"Night"]
# print(data)

#delete the column "shift"
del data['shift']
# print(data)

#delete the row of E101 and E104
employee=data.drop(['E101','E104'])
# print(employee)

#rename the column salary
data.rename(columns={"Salary":"Incentive"},inplace=True)
# print(data)

#update the chnages in the original file
data.to_csv('employee.csv',index=False)
print("Yes the data have been saved in your original file")