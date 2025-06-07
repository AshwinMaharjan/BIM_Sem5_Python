import numpy as np
newArray=np.array([1,2,3,4,5,6,7,8,9,10])
print(newArray[1:5]) #2,3,4,5

print(newArray[4:]) #5,6,7,8,9,10

print(newArray[:4]) #1,2,3,4

#Negative Slicing
print(newArray[-7:-1]) #4,5,6,7,8,9
#steps
#[start:end:steps] -> skip garne

print(newArray[1:5:2]) #2,4

print(newArray[::3]) #1,4,7,10

#slicing 2D array
twoDimArray=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(twoDimArray[1,0:4]) #6,7,8,9

print(twoDimArray[0:2,3]) #4,9

print(twoDimArray[0:2,0:2]) #1,2,6,7