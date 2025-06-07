
#create account class with 2 attributes: balance and account number
class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    #debit method
    def debit(self,amount):
        self.balance =self.balance-amount
        print("Rs.",amount,"was debited from your account.")
    
    #credit method
    def credit(self,amount):
        self.balance=self.balance+amount
        print("Rs.",amount,"was credited to your account.")

    def result(self):
        print("Balance: {}".format(self.balance))
        print("Account Number: {}".format(self.acc_no))

acc1=Account(90000,9876543346)
acc1.result()
acc1.debit(1000)
acc1.credit(2000)
acc1.result()