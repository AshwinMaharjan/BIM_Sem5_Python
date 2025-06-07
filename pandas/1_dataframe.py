import pandas as pd

data1={
       "name":["ashwin","soyal","nishan"], 
       "address": ["nayabazar","patan","kathmandu"],
       "marks":[70,80,90]
       }
data2=pd.DataFrame(data1)

print(data2)

#locate row 
print(data2.loc[0])
print(data2.loc[[0,1]])

#naming the index
data2=pd.DataFrame(data1,index=[101,105,106])
print(data2)
