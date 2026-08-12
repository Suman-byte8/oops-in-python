from models.bank_account import BankAccount
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.storage import save

# Test data
accounts_data = [
    ("7382687677967", "savings", "Patricia Miller", 45000),
    ("1926809822292", "savings", "Barbara Miller", 563654),
    ("3438262463", "savings", "Elizabeth Hernandez", 45789),
    ("5680210264842", "savings", "Robert Johnson", 50000),
    ("01759275672826306", "savings", "Jennifer Lopez", 106500),
    ("44421495038829730", "current", "John Lopez", 3546458),
    ("9442754917159", "current", "Barbara Smith", 456588),
    ("842203480", "current", "David Rodriguez", 12457899),
    ("4780887392", "current", "William Rodriguez", 45789654),
    ("923819834762", "current", "Robert Davis", 354687)
]

# Create accounts
for acc_num, acc_type, name, balance in accounts_data:
    if acc_type == "savings":
        account = SavingsAccount(acc_num, acc_type, name, balance)
    else:
        account = CurrentAccount(acc_num, acc_type, name, balance)
    account.create_account()

# Test Deposit
# print("\n--- Testing Deposit ---")
# test_acc_num = "7382687677967" # Patricia Miller's savings account
# test_acc_type = "savings"
# deposit_amount = 1000

# Calling the deposit method
# account.deposit(deposit_amount, test_acc_num, test_acc_type)
# account.deposit(15000, "44421495038829730", 'current')      # John Lopez's current account


# Test Withdrawal
account.withdraw(1000, "44421495038829730", 'current')      # John Lopez's current account
account.withdraw(44500, "7382687677967", 'savings')      # Patricia Miller's savings account











# print(savings_account.get_balance())        # 1000
# savings_account.withdraw(500)               # Minimum balance of 500 required (1000 - 500 <= 500)
# print(savings_account.get_balance())        # 1000   
# savings_account.withdraw(1500)              # Insufficient balance (1500 > 1000)
# print(savings_account.get_balance())        # 1000
# savings_account.close_account()             # Account 123456 closed successfully



# print(current_account.get_balance())        # 2000
# current_account.withdraw(1000)              # Minimum balance of 1000 required (2000 - 1000 <= 1000)
# print(current_account.get_balance())        # 1000
# current_account.withdraw(3000)              # Insufficient balance (3000 > 2000)
# print(current_account.get_balance())        # 2000
# current_account.withdraw(500)               # Withdrawal of 500 successful
# print(current_account.get_balance())        # 1500
# current_account.close_account()             # Account 789012 closed successfully





