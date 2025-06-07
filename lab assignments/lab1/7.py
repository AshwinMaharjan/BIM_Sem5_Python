# Function to count odd and even numbers in a list
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

# Input from the user
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Count odd and even numbers
odd_count, even_count = count_odd_even(numbers)

# Display the results
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")
