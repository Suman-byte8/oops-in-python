from models.bank_account import BankAccount
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.storage import save




savings_account = SavingsAccount("123456", "savings", "Alice", 1000)
savings_account.create_account()            # Savings account created successfully for Alice
print(savings_account.get_balance())        # 1000
savings_account.withdraw(500)               # Minimum balance of 500 required (1000 - 500 <= 500)
print(savings_account.get_balance())        # 1000   
savings_account.withdraw(1500)              # Insufficient balance (1500 > 1000)
print(savings_account.get_balance())        # 1000
savings_account.close_account()             # Account 123456 closed successfully


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





