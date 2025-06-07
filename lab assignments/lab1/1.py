# Read two numbers from the user
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

# a. Display binary equivalent of the numbers
print(f"Binary of x ({x}): {bin(x)}")
print(f"Binary of y ({y}): {bin(y)}")

# b. Perform bitwise AND, OR, and XOR operations and display results in binary
and_result = x & y
or_result = x | y
xor_result = x ^ y

print(f"Binary of x & y: {bin(and_result)}")
print(f"Binary of x | y: {bin(or_result)}")
print(f"Binary of x ^ y: {bin(xor_result)}")

# c. Perform one's complement of x and display the result in binary format
ones_complement = ~x
print(f"One's complement of x ({x}): {bin(ones_complement)}")

# d. Left shift the x by 3 positions and display the result in binary format
left_shift_x = x << 3
print(f"x left shifted by 3 positions: {bin(left_shift_x)}")

# e. Left shift the y by 2 positions and display the result in binary format
left_shift_y = y << 2
print(f"y left shifted by 2 positions: {bin(left_shift_y)}")
