import pandas as pd

data1={'Name':['Ashwin','Soyal','Joyash','Rojina','Rojan'],
       'Marks':[80,90,98,78,67],
       'Address':['Kathmandu','Pkr','Bkt','Illam','Dolkha'],
       'Age':[20,21,21,22,23],
       'Faculty':['BIM','BBA','BCA','BBM','BCSIT'],
       
       }

data2=pd.DataFrame(data1)
print(data2)

print("Head Function Print:")
print(data2.head(2))

print("Tail Function Print:")
print(data2.tail(2))

