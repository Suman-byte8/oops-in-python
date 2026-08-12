
from models.storage import save
from abc import ABC, abstractmethod
from models.storage import data


class BankAccount(ABC):

    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_holder_name = account_holder_name
        self.initial_balance = initial_balance
        self.balance = initial_balance

# create account
    def create_account(self):
        if self.account_type == "current":
            for account in data['current_accounts']:
                if self.account_number == account['account_number']:
                    print("Account number already exists")
                    return
            
            data['current_accounts'].append({
                'account_number': self.account_number,
                'account_type': self.account_type,
                'account_holder_name': self.account_holder_name,
                'initial_balance': self.initial_balance,
                'balance': self.balance
            })
            print(f"Current account created successfully for {self.account_holder_name}")
            save()

        elif self.account_type == "savings":
            for account in data['savings_accounts']:
                if self.account_number == account['account_number']:
                    print("Account number already exists")
                    return
            
            data['savings_accounts'].append({
                'account_number': self.account_number,
                'account_type': self.account_type,
                'account_holder_name': self.account_holder_name,
                'initial_balance': self.initial_balance,
                'balance': self.balance
            })
            print(f"Savings account created successfully for {self.account_holder_name}")
            save()
        else:
            print("Invalid account type")


# deposit
    def deposit(self, amount, account_number, account_type):
        key = f"{account_type}_accounts"
        for account in data[key]:
            if account['account_number'] == account_number:
                account['balance'] += amount
                save()
                print(f"Deposit of {amount} successful to {account_number}")
                return
        print("Account not found")

# withdraw
    def withdraw(self, amount, account_number, account_type):
        key = f"{account_type}_accounts"

        for account in data[key]:
            if account['account_number'] == account_number:
                if amount > account['balance']:
                    print("Insufficient balance")
                    return
                
                if account_type == "current":
                    if account['balance'] - amount < 1000:
                        print('Minimum balance of 1000 required')
                        return
                else: # savings
                    if account['balance'] - amount < 500:
                        print('Minimum balance of 500 required')
                        return
                
                account['balance'] -= amount
                save()
                print(f"Withdrawal of {amount} successful from {account_number}")
                print(f"New balance: {account['balance']}")
                return
        
        print("Account not found")


# get balance
    def get_balance(self):
        return self.balance

# transfer
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transfer of {amount} successful")
        else:
            print("Insufficient balance")

# get account info
    def get_account_info(self):
        return f"Account Number: {self.account_number}, Account Type: {self.account_type}, Account Holder Name: {self.account_holder_name}, Initial Balance: {self.initial_balance}, Current Balance: {self.balance}"

# close account
    def close_account(self):
        print(f"Account {self.account_number} closed successfully")
