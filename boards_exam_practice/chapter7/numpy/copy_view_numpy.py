import numpy as np

#copy
array1=np.array([1,2,3,4,5])
array2=array1.copy()
array2[0]=10
print(array1) #1,2,3,4,5
print(array2) #10,2,3,4,5

#view
array3=np.array([6,7,8,9,10])
array4=array3.view()
array4[0]=60
print(array3) #60,7,8,9,10
print(array4) #60,7,8,9,10