class Student:
    def __init__(self,name,age):
        self.__name=name #private variable
        self.__age=age #private variable

    def __display(self): #private method
        print("Name: ",self.__name)
        print("Age: ",self.__age)
        
    def show(self):
        self.__display #accessbile

stud=Student("Ashwin",20)
print(stud.__name) #error 
print(stud.__age) #error
stud.__display() #error
stud.show() #accessible