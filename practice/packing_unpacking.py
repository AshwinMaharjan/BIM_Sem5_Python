def greet(name, age):
    print(f"Hello {name}, age {age}")

student = ("Ashwin", 20)
greet(*student)   # Unpacks to greet("Ashwin", 20)


def greet(name, age):
    print(f"Hello {name}, age {age}")

student_info = {"name": "Ashwin", "age": 20}
greet(**student_info)  # Unpacks to greet(name="Ashwin", age=20)
