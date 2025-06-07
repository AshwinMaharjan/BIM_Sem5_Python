class College():
    def __init__(self,cname):
        self.cname=cname
    
    # @staticmethod
    # def hello():
    #     print("Helloo")

class Student(College):
    def __init__(self,sname,age,cname):
        super().__init__(cname)
        self.sname=sname
        self.age=age
    
    def display(self):
        print("Student Name: ",self.sname)
        print("Student Age: ",self.age)
        print("College Name: ",self.cname)

s1=Student("Ashwin",20,"Prime College")
s1.display()

        