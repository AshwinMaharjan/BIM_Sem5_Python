class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

std=Student("Ashwin",20)
print(std.name) #accessible
print(std.age) #accessbile
std.display() #accessible
