import numpy as np

#indexing the 1d array
newArray=np.array([1,2,3,4,5])
print(newArray[3]) #4

#indexing the 2d array
newArray=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(newArray[1,3]) #9

#indexing the 3d array
newArray=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(newArray[0,1,2]) #6

