class Student:
    def welcome(self):
        print("Welcome Student")
    
class Employee(Student):
    def welcome(self):
        # super().welcome() 
        print("Welcome Employee")

emp=Employee()
emp.welcome()
