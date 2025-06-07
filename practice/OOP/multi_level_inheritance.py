class University:
    @staticmethod
    def uni():
        return("Tribhuvan Univeristy")

class College(University):
    @staticmethod
    def college():
        return("Prime College")
    
class Student(College):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

s1=Student("Ashwin",20)
s1.display() #name and age is displayed

print("You study in", s1.college())
print("You belong to", s1.uni())
