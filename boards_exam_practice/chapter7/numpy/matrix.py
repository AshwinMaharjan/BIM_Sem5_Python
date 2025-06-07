import numpy as np

array1=np.random.randint(1,15,size=(3,3))
array2=np.random.randint(1,15,size=(3,3))
array3=np.dot(array1,array2)
print(array3)
