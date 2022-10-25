# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class
# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info


class Bank_account:
    all_bank_accounts=[]
    def __init__(self,balance, int_rate):
        self.balance=balance
        self.int_rate=int_rate
        Bank_account.all_bank_accounts.append(self)

    def deposit(self, amount):
        self.amount= amount
        self.balance= self.balance + amount
        return self

    def withdraw(self, amount):
        self.amount= amount
        self.balance= self.balance - amount
        return self
    
    def display_info(self):
        print(f' Balance:{self.balance} interest rate:{self.int_rate} yield_int: {self.yield_int}')
    
    def yield_int(self):
        self.yield_int = self.balance * self.int_rate
        return self

# kevin=Bank_account(100,.10)
# kevin.deposit(10),kevin.deposit(10),kevin.deposit(10),kevin.withdraw(10),kevin.yield_int(),kevin.display_info()

# kevin2=Bank_account(100,.10)
# kevin2.deposit(100), kevin2.deposit(100), kevin2.deposit(100), kevin2.withdraw(10), kevin2.withdraw(10), kevin2.withdraw(10) 
# kevin2.withdraw(10),kevin2.yield_int(), kevin2.display_info()

# print(Bank_account.all_bank_accounts.__repr__)