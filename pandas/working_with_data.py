import pandas as pd

data=pd.read_csv('data.csv',index_col=0)
print(data)

#rename the count of pencil
data.Count['Eraser']=15
print(data)