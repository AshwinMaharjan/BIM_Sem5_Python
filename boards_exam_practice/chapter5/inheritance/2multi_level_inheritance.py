class University:
    @staticmethod
    def uni():
        return "TU"
    
class College(University):
    @staticmethod
    def clg():
        return "Prime"

class Student(College):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_result(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        # print("University: ",self.uni())
        # print("College: ",self.clg())
        
student=Student("Ashwin",21)
print(student.uni())
print(student.clg())
student.show_result()