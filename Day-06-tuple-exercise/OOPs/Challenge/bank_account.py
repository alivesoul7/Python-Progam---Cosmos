class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error : Insufficient funds!")
        else:
            self.balance = self.balance -  amount
            print(f"Amount {amount} is withdrawn")

    def check_balance(self):
        print(f"Current Balance: { self.balance}")

acc = BankAccount()
acc.deposit(80000)
acc.withdraw(30000)
acc.check_balance()