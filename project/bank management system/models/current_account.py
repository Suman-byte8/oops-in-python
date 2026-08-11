from models.bank_account import BankAccount
from models.storage import save, data


# current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)

    # create account
    def create_account(self):
        if self.account_type == "current":
            print(f"Current account created successfully for {self.account_holder_name}")
            data['current_accounts'].append({
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
            # check if minimum balance is met
            if self.balance - amount <=1000:
                print('Minimum balance of 1000 required')
                return

            self.balance -= amount
            
            # update stored account balance
            for account in data['current_accounts']:
                if account['account_number'] == self.account_number:
                    account['balance'] = self.balance
                    break

            save()

            print(f"Withdrawal of {amount} successful")
            print(f"New balance: {self.balance}")


        else:
            print("Insufficient balance")
