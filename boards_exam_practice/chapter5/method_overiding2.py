class College:
    @staticmethod
    def show():
        print("College Name")
        
class Student(College):
    @staticmethod
    def show():
        print("Student Name")

s=Student()
s.show()