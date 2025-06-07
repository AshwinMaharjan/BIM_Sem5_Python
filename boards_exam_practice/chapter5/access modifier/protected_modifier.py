class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _showinfo(self):
        print("Name: ",self._name) #accessible
        print("Age: ",self._age) #accessbile

class GraduateStudent(Student):
    def show(self):
        print("Name: ",self._name)
        print("Age: ",self._age)
    
student=GraduateStudent("Ashwin",21)
print(student._name) #no error but not recommended
print(student._age)#no error but not recommended
student._showinfo()#no error but not recommended
student.show()
