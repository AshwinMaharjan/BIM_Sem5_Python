
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, Id, name, age):
        self.Id = Id
        self.name = name
        self.age = age

    @abstractmethod
    def getData(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Employee(Person):
    def __init__(self, Id, name, age, salary):
        super().__init__(Id, name, age)
        self.salary = salary

    def getData(self):
        self.salary = float(input("Enter salary: "))

    def display(self):
        print(f"Employee: {self.Id}, {self.name}, {self.age}, Salary: {self.salary}")

class Customer(Person):
    def __init__(self, Id, name, age, credit_rating):
        super().__init__(Id, name, age)
        self.credit_rating = credit_rating

    def getData(self):
        self.credit_rating = int(input("Enter credit rating: "))

    def display(self):
        print(f"Customer: {self.Id}, {self.name}, {self.age}, Credit Rating: {self.credit_rating}")

emp = Employee(101, "Alice", 30, 50000)
cust = Customer(201, "Bob", 25, 750)

emp.display()
cust.display()
