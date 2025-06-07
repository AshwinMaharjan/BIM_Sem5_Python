class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Ashwin",21)
s2=Student("Nupur",19)

print("Student Name:{} and Age:{}".format(s1.name,s1.age))
print("Student Name:{} and Age:{}".format(s2.name,s2.age))
