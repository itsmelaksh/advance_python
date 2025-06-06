# Example file for Advanced Python by Joe Marini
# Defining and using custom exceptions in Python

# Define a custom exception class
class InsufficientFundsError(Exception):
    """Raised when the account balance is insufficient for a transaction."""
    def __init__(self, balance, amount):
        message = f"Insufficient balance: ${balance:.2f} (required: ${amount:.2f})"
        super().__init__(message)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (amount > self.balance):
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Create a bank account with an initial balance of $100
account = BankAccount(100)

try:
    account.deposit(10)
    # should work
    account.withdraw(50)
    # Attempt to withdraw $100, which exceeds the balance
    account.withdraw(100)
except InsufficientFundsError as e:
    print(f"Error: {e}")
else:
    print("Withdrawal successful.")
finally:
    print(f"Current balance: ${account.get_balance():.2f}")
