from models.bank_account import BankAccount
from models.storage import save, data


# savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)

    # create account
    def create_account(self):
        if self.account_type == "savings":
            print(f"Savings account created successfully for {self.account_holder_name}")
            data['savings_accounts'].append({
                'account_number': self.account_number,
                'account_type': self.account_type,
                'account_holder_name': self.account_holder_name,
                'initial_balance': self.initial_balance,
                'balance': self.balance
            })

            save()
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
