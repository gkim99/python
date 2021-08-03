class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print{f"Balance: ${balance}"}
        return self 

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

rawr = BankAccount(0.01, 200)
moo = BankAccount(0.02, 800)

rawr.deposit(300).deposit(500).deposit(100).withdraw(300).yield_interest().display_account_info()
moo.deposit(300).deposit(700).withdraw(100).withdraw(200).withdraw(150).withdraw(90).yield_interest().display_account_info()