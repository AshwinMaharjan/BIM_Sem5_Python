class Account:
    def __init__(self, acc_no, acc_name, balance):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.acc_no}, Name: {self.acc_name}, Balance: {self.balance}")

class SavingAccount(Account):
    min_balance = 500  # Class variable

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.verify(amount):
            self.balance -= amount
            print("Withdraw successful!")
        else:
            print("Insufficient balance!")

    def transfer(self, amount, to_account):
        if self.verify(amount):
            self.balance -= amount
            to_account.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient balance!")

    @classmethod
    def displayMinBalance(cls):
        print(f"Minimum Balance: {cls.min_balance}")

    @staticmethod
    def verify(amount):
        return amount >= 0 and amount <= SavingAccount.min_balance

# Example usage
acc1 = SavingAccount(101, "Alice", 1000)
acc2 = SavingAccount(102, "Bob", 800)

acc1.withdraw(200)
acc1.transfer(100, acc2)
acc1.display()
acc2.display()
SavingAccount.displayMinBalance()
