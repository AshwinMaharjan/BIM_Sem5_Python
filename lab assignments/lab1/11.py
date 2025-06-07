import math

# Function to find square root of a number
def find_square_root(num):
    return math.sqrt(num)

# Input: List of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Use map to apply find_square_root function to all elements of the list
square_roots = list(map(find_square_root, numbers))

# Display the results
print("\nSquare roots of the numbers:")
for num, root in zip(numbers, square_roots):
    print(f"Square root of {num}: {root}")
