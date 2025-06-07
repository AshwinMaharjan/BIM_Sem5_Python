from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @abstractmethod
    def display_details(self): #abstract method
        pass

class GraduateStudent(Student):
    def display_details(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

stud=GraduateStudent("Ashwin",20)
print(stud.name)
print(stud.age)
stud.display_details()