#same method name for both parent and child class

class College:
    def __init__(self,cname):
        self.cname=cname
    def result(self):
        print("College Name: ",self.cname)

class Student(College):
    def __init__(self,sname,age,cname):
        self.sname=sname
        self.age=age
        super().__init__(cname)
    def result(self):
        print("Student Name: ",self.sname)
        print("Student Age: ",self.age)
        print("College Name: ",self.cname)

student=Student("Ashwin",21,"Prime")
student.result()


        