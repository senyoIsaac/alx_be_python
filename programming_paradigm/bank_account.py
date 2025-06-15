class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # private attribute

    # Getter method
    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
        # Alternatively, could return the balance:
        # return self.balance

    # Setter method with validation
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")
      

"""
# Using the class
account = BankAccount("Alice", 1000)

# Try to access private attribute directly (won't work as intended)
# print(account.__balance)  # ❌ AttributeError

# Can't access __balance directly
print(account.get_balance())  # ✅ 1000


account.deposit(500)
print(account.get_balance())  # ✅ 1500

account.withdraw(2000)  # ❌ Insufficient balance
"""
