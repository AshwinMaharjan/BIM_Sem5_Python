# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input: List of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Use filter to apply is_prime function to all elements of the list
prime_numbers = list(filter(is_prime, numbers))

# Display the results
print("\nPrime numbers in the list:")
print(prime_numbers)
