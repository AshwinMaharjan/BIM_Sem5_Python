import math

# Function to calculate the factorial of each number
def calculate_factorials(*numbers):
    results = {}
    for num in numbers:
        if num >= 0:  # Factorial is defined for non-negative integers
            results[num] = math.factorial(num)
        else:
            results[num] = "Undefined (factorial is not defined for negative numbers)"
    return results

# Accept a variable number of arguments from the user
nums = input("Enter numbers separated by spaces: ").split()
nums = [int(num) for num in nums]  # Convert input strings to integers

# Calculate factorials
factorial_results = calculate_factorials(*nums)

# Display the results
print("\nFactorials:")
for num, fact in factorial_results.items():
    print(f"{num}! = {fact}")
