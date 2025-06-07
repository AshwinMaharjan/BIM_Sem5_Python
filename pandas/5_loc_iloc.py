import pandas as pd

data1={
    'Name':['Ashwin','Soyal','Rojina'],
    'Age':[20,23,22],
    'Address':['Nayabazar','Nardevi','Basantapur']
}

data2=pd.DataFrame(data1)
print(data2.to_string())

#loc slicing 
print("----------------------")
print("Loc Slicing")

data3=data2.loc[0:3,['Name','Address']] #ja samma vaneko xa teta samma gardinxa print
print(data3)

#iloc slicing
print("----------------------")
print("Iloc Slicing")

data3=data2.iloc[0:2,[0,2]] #last index include hudaina but loc ma chai vako thiyooo
print(data3)
