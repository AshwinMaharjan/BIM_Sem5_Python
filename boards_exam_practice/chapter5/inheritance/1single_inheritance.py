class Country:
    def __init__(self,name):
        self.name=name
    def welcome(self):
        print("Welcome to",self.name)

class City(Country):
    def __init__(self,name):
        super().__init__(name)

c1=City("Nepal")
c2=City("Kathmandu")

c1.welcome()
c2.welcome()

        
