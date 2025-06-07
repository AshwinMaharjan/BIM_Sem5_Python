import pandas as pd

data1={
    'Name':['Ashwin','Nupur','Rojina','Rojan','Soyal'],
    'Age':[21,22,23,22,24],
    'Marks':[90,70,80,55,67],
    'Address':['Kathmandu','India','Australia','China','USA'],
    'Faculty':['BIM','BCA','BIM','BBM','BBA']

}

data2=pd.DataFrame(data1)
slice_row=data2.loc[0:3]
print(slice_row) #soyal aaudaina

slice_row2=data2.iloc[0:3]
print(slice_row2) #rojina,soyal aaudaina

slice_row3=data2.loc[0:3,['Name','Age']]
print(slice_row3)

slice_row4=data2.loc[:,['Name','Age']]
print(slice_row4)



