class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area_of_rectangle(self):
        return self.length * self.breadth
    def perimeter_of_rectangle(self):
        return 2 * (self.length + self.breadth)

class Square:
    def __init__(self,length):
        self.length=length
    def area_of_square(self):
        return self.length * self.length
    def perimeter_of_square(self):
        return 4 * self.length

shape = Rectangle(3,5)
print("Area of rectangle: ",shape.area_of_rectangle())
print("Perimeter of rectangle: ",shape.perimeter_of_rectangle())

shape2 = Square(5)
print("Area of square: ",shape2.area_of_square())
print("Perimeter of square: ",shape2.perimeter_of_square())
