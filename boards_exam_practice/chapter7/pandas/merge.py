import pandas as pd

#merging the data
data1={
    'id':[101,102,103,104],
    'Name':['Ashwin','Nupur','Rojina','Joyash'],
    'Age':[21,22,23,22],
}
data2={
    'id':[101,102,103,105],  
    'Address':['Kathmandu','Nepal','India','China'],
    'Faculty':['BIM','BBA','BBS','BBM'],
    'Marks':[90,78,88,65]

}
data3=pd.DataFrame(data1)
data4=pd.DataFrame(data2)
result=pd.merge(data3,data4,on='id',how='inner')
print(result)

