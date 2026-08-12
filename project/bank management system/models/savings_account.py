from models import bank_account
from models.bank_account import BankAccount
from models.storage import save, data


# savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)

