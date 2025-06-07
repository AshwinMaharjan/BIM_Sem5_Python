
class Customer:
    def __init__(self, Cid, Cname, Address):
        self.Cid = Cid
        self.Cname = Cname
        self.Address = Address

    def display(self):
        print(f"Customer ID: {self.Cid}, Name: {self.Cname}, Address: {self.Address}")

class Employee:
    def __init__(self, Eid, Ename, Post):
        self.Eid = Eid
        self.Ename = Ename
        self.Post = Post

    def display(self):
        print(f"Employee ID: {self.Eid}, Name: {self.Ename}, Post: {self.Post}")

class EmpCustomer(Customer, Employee):
    def __init__(self, Cid, Cname, Address, Eid, Ename, Post, rating):
        Customer.__init__(self, Cid, Cname, Address)
        Employee.__init__(self, Eid, Ename, Post)
        self.rating = rating

    def display(self):
        super().display()
        print(f"Rating: {self.rating}")

emp_cust = EmpCustomer(1, "John", "NY", 101, "John Doe", "Manager", 5)
emp_cust.display()
