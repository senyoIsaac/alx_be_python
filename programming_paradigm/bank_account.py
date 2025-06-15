class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print(f"Current Balance:${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew:${amount}")
    