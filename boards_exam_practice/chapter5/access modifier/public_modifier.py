class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)

student=Student("Ashwin",21)
print(student.name)
print(student.age)
student.show_info()