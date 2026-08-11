from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_holder_name = account_holder_name
        self.initial_balance = initial_balance
        self.balance = initial_balance

# create account
    @abstractmethod
    def create_account(self):
        pass

# deposit
    def deposit(self, amount):
        self.balance += amount

# withdraw
    @abstractmethod
    def withdraw(self, amount):
        pass

# get balance
    def get_balance(self):
        return self.balance

# transfer
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balanceposit(amount)
            print(f"Transfer of {amount} successful")
        else:
            print("Insufficient balance")

# get account info
    def get_account_info(self):
        return f"Account Number: {self.account_number}, Account Type: {self.account_type}, Account Holder Name: {self.account_holder_name}, Initial Balance: {self.initial_balance}, Current Balance: {self.balance}"

# close account
    def close_account(self):
        print(f"Account {self.account_number} closed successfully")
