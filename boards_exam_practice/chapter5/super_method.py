class College:
    def __init__(self,cname):
        self.cname=cname
    def collegeName(self):
        return self.cname
    
class Student(College):
    def __init__(self,sname,age,cname):
        self.sname=sname
        self.age=age
        super().__init__(cname)
    def show_result(self):
        print("Student Name: ",self.sname)
        print("Student Age: ",self.age)
        print("College Name: ",self.cname)

stud=Student("Ashwin",21,"Prime College")
stud.show_result()


    
        