class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "accepted. Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of", amount, "processed. Current balance:", self.balance)
        else:
            print("Insufficient funds! Withdrawal amount exceeds available balance.")
