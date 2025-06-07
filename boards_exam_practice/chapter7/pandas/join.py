import pandas as pd

#joining the data
data1={
    'Name':['Ashwin','Nupur','Rojina','Joyash'],
    'Age':[21,22,23,22],
}
data2={
    'Address':['Kathmandu','Nepal','India','China'],
    'Faculty':['BIM','BBA','BBS','BBM'],
    'Marks':[90,78,88,65]
}
data3=pd.DataFrame(data1, index=[101,102,103,104])
data4=pd.DataFrame(data2, index=[101,102,103,104])
result=data3.join(data4, how='inner')
print(result)