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


# savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)

    # create account
    def create_account(self):
        if self.account_type == "savings":
            print(f"Savings account created successfully for {self.account_holder_name}")
        else:
            print("Invalid account type")

    # withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            if self.balance - amount <=500:
                print('Minimum balance of 500 required')
            else:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful")
        else:
            print("Insufficient balance")


# current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)

    # create account
    def create_account(self):
        if self.account_type == "current":
            print(f"Current account created successfully for {self.account_holder_name}")
        else:
            print("Invalid account type")

    # withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            # check if minimum balance is met
            if self.balance - amount <=1000:
                print('Minimum balance of 1000 required')
            else:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful")
        else:
            print("Insufficient balance")


# savings_account = SavingsAccount("123456", "savings", "Alice", 1000)
# savings_account.create_account()            # Savings account created successfully for Alice
# print(savings_account.get_balance())        # 1000
# savings_account.withdraw(500)               # Minimum balance of 500 required (1000 - 500 <= 500)
# print(savings_account.get_balance())        # 1000   
# savings_account.withdraw(1500)              # Insufficient balance (1500 > 1000)
# print(savings_account.get_balance())        # 1000
# savings_account.close_account()             # Account 123456 closed successfully


# current_account = CurrentAccount("789012", "current", "Bob", 2000)
# current_account.create_account()            # Current account created successfully for Bob
# print(current_account.get_balance())        # 2000
# current_account.withdraw(1000)              # Minimum balance of 1000 required (2000 - 1000 <= 1000)
# print(current_account.get_balance())        # 1000
# current_account.withdraw(3000)              # Insufficient balance (3000 > 2000)
# print(current_account.get_balance())        # 2000
# current_account.withdraw(500)               # Withdrawal of 500 successful
# print(current_account.get_balance())        # 1500
# current_account.close_account()             # Account 789012 closed successfully





