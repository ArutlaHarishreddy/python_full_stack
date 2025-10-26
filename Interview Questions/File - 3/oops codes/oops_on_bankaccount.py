#Create a class `BankAccount` with methods `deposit`, `withdraw`, and `check_balance`.
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder=holder
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance = self.balance+amount
            print("Deposit $",amount,". New balance: $",self.balance)
        else:
            print("Deposite amount must be Positive")
    
    def withdraw(self, amount):
        if amount<=self.balance and amount>0:
            self.balance=self.balance-amount
            print("Withdraw amount is:",amount, ", New balance is:",self.balance)
        else:
            print("The withdraw amount should be positive and less than or equal to Account balance")
    def check_balance(self):
        print("Your Account balance is:", self.balance)

account=BankAccount("Harish",1000)
account.check_balance()
account.withdraw(400)
account.deposit(500)