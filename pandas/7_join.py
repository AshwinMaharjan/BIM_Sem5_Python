import pandas as pd

data1={
    "Key":[0,1,2,3],
    "Name":["Ashwin","Rojan","Nishan","Rojina"],
    "Age":[20,21,21,22],
    "Address":["India","Nepal","Pakistan","China"]
}

data2={
    "Key":[0,1,2,3],
    "Qualification":["BIM","BBA","BCA","BBM"],
    "Marks":[90,87,77,89],
}

data3=pd.DataFrame(data1)
data4=pd.DataFrame(data2)

data5=pd.merge(data3,data4,on='Key',how='left')
print(data5)