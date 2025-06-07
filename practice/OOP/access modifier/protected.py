class Student:
    def __init__(self,name,age):
        self._name=name #protected variable
        self._age=age #protected variable
    def _display(self): #protected method
        print("Name: ",self._name)
        print("Age: ",self._age)

class GraduateStudent(Student):
    def show(self):
        print("Name: ",self._name) #accessbile in subclass

stud=GraduateStudent("Ashwin",20)
print(stud._name) # no error but not recomended
print(stud._age)  # no error but not recomended
stud._display() #no error but not recomended
stud.show() #accessible
        