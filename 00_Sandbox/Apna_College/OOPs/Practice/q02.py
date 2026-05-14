# Create Account class with 2 Attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was deleted")
        print("Total Balance = ", self.get_balance())


    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance())


    def get_balance(self):
        return self.balance


acc1 = Account(8000, 25161)
acc1.debit(1000)
acc1.credit(5000)