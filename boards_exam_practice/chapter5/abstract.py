# class Car:
#     def __init__(self):
#         self.acc=True
#         self.brake=True
#         self.clutch=True
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car is now started")
# car=Car()
# car.start()

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):  # Concrete class
    def start(self):
        print("Car is now started")

car = Car()
car.start()
