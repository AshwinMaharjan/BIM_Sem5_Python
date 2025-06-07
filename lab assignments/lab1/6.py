# Function to find the second largest element
def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two distinct elements."

    largest = second_largest = float('-inf')  # Initialize as negative infinity

    for num in numbers:
        if num > largest:  # Update largest and second largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:  # Update second largest
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element (all elements are the same)."

    return second_largest

# Input from user
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Find the second largest element
result = find_second_largest(numbers)

# Display the result
print(f"Second largest element: {result}")
