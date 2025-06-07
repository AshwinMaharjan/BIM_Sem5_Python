#method overloading is not supported in python
class Math:
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b 

    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        return self.a+self.b+self.c

math=Math()
print("Result: ".format(math.add(1,2)))
print("Another Result: ".format(math.add(3,4,5)))
    