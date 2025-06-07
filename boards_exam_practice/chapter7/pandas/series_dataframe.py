import pandas as pd
data1={
    'Name':['Ashwin','Nupur','Rojina','Rojan','Soyal'],
    'Age':[21,22,23,22,24],
    'Marks':[90,70,80,55,67],
    'Address':['Kathmandu','India','Australia','China','USA'],
    'Faculty':['BIM','BCA','BIM','BBM','BBA']
}
data2=pd.DataFrame(data1)
data3=pd.Series(data1['Marks'])

print(data2)
print("\n")
print(data3)
