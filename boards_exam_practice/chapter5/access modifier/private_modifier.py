class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def __show(self):
        print("Student Name: ",self.__name)
        print("Student Age: ",self.__age)
    def result(self):
        self.__show()

stud=Student("Ashwin",21)
print(stud.__name) #ERROR
print(stud.__age) #ERROR
stud.__show() #ERROR
stud.result() #accessible