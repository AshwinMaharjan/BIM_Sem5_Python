# Read two complex numbers from the user
num1 = complex(input("Enter the first complex number (e.g., 2+3j): "))
num2 = complex(input("Enter the second complex number (e.g., 1+2j): "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if the second number is not zero before performing division
if num2 != 0:
    division = num1 / num2
else:
    division = "Division by zero is not defined"

# Display results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
