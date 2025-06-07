import pandas as pd

data1={
    "Name":["Ashwin","Rojan","Nishan","Rojina"],
    "Age":[20,21,21,22],
    "Address":["India","Nepal","Pakistan","China"]
}

data2={
    "Name":["Soyal","Yujal","Joyash","Sakku"],
    "Age":[18,19,18,24],
    "Address":["India","Nepal","Pakistan","China"]
}

data3=pd.DataFrame(data1, index=[0,1,2,3])
data4=pd.DataFrame(data2, index=[4,5,6,7])

frames=[data3,data4]
print(pd.concat(frames))

