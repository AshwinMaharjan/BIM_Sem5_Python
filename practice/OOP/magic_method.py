#__str__(self)
class Student:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return "Name:{}".format(self.name)

stud=Student("Ashwin")
print(stud.__str__())

#__repr__(self)
class Employee:
    def __init__(self,age):
        self.age=age
    
    def __repr__(self):
        return "Age:{}".format(self.age)

emp=Employee(20)
print(repr(emp))

#__add__(self,other)
class GraduateStudent():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def __add__(self,other):
        return self.marks+other.marks

g1=GraduateStudent("Ashwin",90)
g2=GraduateStudent("Anjali",80)
total_marks=g1+g2
print(total_marks)

#__len__(self)
class Subject:
    def __init__(self,name,subjects):
        self.name=name
        self.subjects=subjects
    def __len__(self):
        return len(self.subjects)

sub=Subject("Ashwin",["Python","AI","Marketing"])
print(len(sub))