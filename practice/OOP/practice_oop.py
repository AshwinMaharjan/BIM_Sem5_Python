#encapsulation

class Student:
    def __init__(self,name,marks,age,address):
        self.name=name
        self.marks=marks
        self.age=age
        self.address=address


s1=Student("Ashwin",90,"","")
s2=Student("","",20,"Nayabazar")
print("Name: {}, Marks: {}".format(s1.name,s1.marks))
print("Age: {}, Address: {}".format(s2.age,s2.address))

