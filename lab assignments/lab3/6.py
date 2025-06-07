import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view_arr = arr.view()  # Creating a view
copy_arr = arr.copy()  # Creating a copy

print("Original Array:", arr)
print("View Array:", view_arr)
print("Copy Array:", copy_arr)

# Modify the view and check impact
view_arr[0] = 10
print("After modifying view array, original array:", arr)  # Changes in view reflect in original

# Modify the copy and check impact
copy_arr[1] = 20
print("After modifying copy array, original array:", arr)  # No change in original

