import numpy as np

arr = np.arange(1, 101)
print("Array Dimension:", arr.ndim)
print("Array Size:", arr.size)

# Check if we can resize to (3,3)
if arr.size == 9:
    arr = arr.reshape(3, 3)
    print(arr)
else:
    print("Cannot reshape as the size is not compatible.")