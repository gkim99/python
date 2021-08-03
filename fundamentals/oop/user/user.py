class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount 

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
    
rawr = User("Rawr")
moo = User("Moo")
boo = User("Boo")

rawr.make_deposit(100)
rawr.make_deposit(200)
rawr.make_deposit(50)
rawr.make_withdrawl(150)
rawr.display_user_balance()

moo.make_deposit(100)
moo.make_deposit(200)
moo.make_withdrawl(50)
moo.make_withdrawl(20)
moo.display_user_balance()

boo.make_deposit(700)
boo.make_withdrawl(100)
boo.make_withdrawl(50)
boo.make_withdrawl(20)
boo.display_user_balance()

rawr.transfer_money(boo, 150)