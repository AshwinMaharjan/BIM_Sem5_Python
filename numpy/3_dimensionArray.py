import numpy as np

a = np.array(11)
print(a)

b = np.array([1,2,3,4])
print(b)

c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c)

d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)