class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello, ",self.name)
        print("Your age is: ",self.age)
s1=Student("Ashwin",20)
s1.greet()
