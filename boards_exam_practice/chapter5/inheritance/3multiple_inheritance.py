class University:
    @staticmethod
    def uni():
        return "TU"
    
class College:
    @staticmethod
    def clg():
        return "Prime College"

class Student(University,College):
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def show_info(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)
        print("Student Address: ",self.address)

student=Student("Ashwin",21,"Nayabazar")
print(student.uni())
print(student.clg())
student.show_info()
        

