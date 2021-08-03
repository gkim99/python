class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount 
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self
    
rawr = User("Rawr")
moo = User("Moo")
boo = User("Boo")

rawr.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(150).display_user_balance()

moo.make_deposit(100).make_deposit(200).make_withdrawl(50).make_withdrawl(20).display_user_balance()

boo.make_deposit(700).make_withdrawl(100).make_withdrawl(50).make_withdrawl(20).display_user_balance()

rawr.transfer_money(boo, 150)