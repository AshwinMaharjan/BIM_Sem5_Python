class College:
    @staticmethod
    def hello():
        print("Heloooo Student")
    
    @staticmethod
    def welcome():
        print("Welcome Student")

class Student(College):
    def __init__(self,name):
        self.name=name

    def display_name(self):
        return self.name
    
s1=Student("Ashwin")
print("Name:{}".format(s1.display_name()))

s1.welcome() #parent class ko method lai call gardai xa
s1.hello() #parent class ko method lai call gardai xa


    