'''
Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
'''
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def calculate_area(self):
        return (3.14 * self.radius * self.radius)
    
    def calculate_perimeter(self):
        return (2 * 3.14 * self.radius)

circle=Circle(3)
print("Area of circle: ",circle.calculate_area())    
print("Perimeter of circle: ",circle.calculate_perimeter())    

# if i want to take input from the user
# take_radius=int(input("Enter the radius: "))
# radius=take_radius
# circle=Circle(radius)
# print("Area of circle: ",circle.calculate_area())    
# print("Perimeter of circle: ",circle.calculate_perimeter())    

