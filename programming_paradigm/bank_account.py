class BankAccount:
    def __init__(self, balance):
        #self.owner = owner
        self.__balance = balance  # private attribute

    # Getter method
    def display_balance(self):
        return self.__balance

    # Setter method with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

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
