from models.bank_account import BankAccount
from models.storage import save, data


# current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)


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
