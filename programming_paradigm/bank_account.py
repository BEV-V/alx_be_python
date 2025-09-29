class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default = 0)."""
        self.__account_balance = initial_balance  # Encapsulation

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds exist.
        Returns True if successful, otherwise False."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance}")
