#<--___
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
from bank_account import Bank_account

class User:
    def __init__(self,data):
        self.first_name=data['first_name']
        self.last_name=data["last_name"]
        self.email=data['email']
        self.age=data['age']
        self.is_rewards_member=False
        self.gold_card_points=0
        self.wells_account= Bank_account(int_rate=.10,balance=0)
        self.chase_account= Bank_account(int_rate=.10,balance=0)

    def display_info(self):
        print(self.first_name,self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member==True:
            print('User already a member')
        else:
            self.gold_card_points=200
            self.is_rewards_member=True
        return self

    def spent(self,amount):
        if amount > self.gold_card_points:
            print('not enough points')
        else:
            self.amount= self.gold_card_points - amount
            print(f'you spent ${amount}')
        return amount
#<---Wells methods-->
    def wells_deposit(self, amount):
        self.wells_account.deposit(amount)
        return self

    def wells_withdraw(self,amount):
        self.wells_account.withdraw(amount)
        return self

    def wells_account_balance(self):
        print(self.wells_account.balance)
        return self

#<---Chase methods-->
    def chase_deposit(self, amount):
        self.chase_account.deposit(amount)
        return self

    def chase_withdraw(self,amount):
        self.chase_account.withdraw(amount)
        return self
    
    def chase_account_balance(self):
        print(self.chase_account.balance)
        return self
    
    # def tranfer(self, amount):
    #     transfer=self.wells_account.deposit(amount)
    #     return transfer



kevin=User({
    'first_name': 'kevin',
    'last_name': 'merz',
    'email': 'kevin@yahpoo.com',
    'age': '30'
})


kevin.wells_deposit(100), kevin.chase_deposit(100), kevin.wells_account_balance(), kevin.chase_withdraw(20), kevin.chase_account_balance()

# kevin2=User({
#     'first_name': 'kevin2',
#     'last_name': 'merz2',
#     'email': 'kevin@yahpoo.com',
#     'age': '30'
# })
# kevin2.enroll(), kevin2.spent(80), kevin2.display_info()


# kevin3=User({
#     'first_name': 'kevin',
#     'last_name': 'merz',
#     'email': 'kevin@yahpoo.com',
#     'age': '30'
# })
# kevin3.display_info(), kevin3.spent(40)