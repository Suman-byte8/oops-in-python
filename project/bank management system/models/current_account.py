from models.bank_account import BankAccount
from models.storage import save, data


# current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_type, account_holder_name, initial_balance):
        super().__init__(account_number, account_type, account_holder_name, initial_balance)


