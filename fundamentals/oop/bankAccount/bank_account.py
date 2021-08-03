class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount): 
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self 

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

rawr = BankAccount(0.01, 1000)
moo = BankAccount(0.02, 800)

rawr.deposit(300).deposit(500).deposit(100).withdraw(300).yield_interest().display_account_info()
moo.deposit(300).deposit(700).withdraw(100).withdraw(200).withdraw(150).withdraw(90).yield_interest().display_account_info()

BankAccount.print_all_accounts()