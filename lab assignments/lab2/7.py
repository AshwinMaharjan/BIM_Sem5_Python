
try:
    arr = [1, 2, 3]
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)  # May cause ZeroDivisionError
    print("Array Element:", arr[5])  # May cause IndexError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except IndexError:
    print("Error: Invalid index.")
finally:
    print("Execution completed.")
