import pandas as pd
data1={
    'Name':['Ashwin','Nupur','Rojina','Rojan','Soyal'],
    'Age':[21,22,23,22,24],
    'Marks':[90,70,80,55,67],
    'Address':['Kathmandu','India','Australia','China','USA'],
    'Faculty':['BIM','BCA','BIM','BBM','BBA'],
    'Roll':[105,106,107,108,109]

}

data2=pd.DataFrame(data1)
print(data2.loc[0]) #series(line by line) aauxa
print(data2.loc[[0,1]]) #tabular format ma jasto aauxa
