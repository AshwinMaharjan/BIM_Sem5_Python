class College():
    @staticmethod
    def college():
        return "Prime College"

class Semester():
    @staticmethod
    def sem():
        return "5th Semester"

class Student(College,Semester):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

s1=Student("Ashwin",20)
s1.display()
print("You study in ",s1.sem())
print("You study in ",s1.college())

