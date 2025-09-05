import random

class BankAccount:
    def __init__(self, name, balance, isAdmin = False):
        promo_price = 2000
        acct_number = int(random.random() * 10000000000)
          
        if random.random() < 0.5:
            self.hasPromo = True
        else:
            self.hasPromo = False

        if self.hasPromo:
            self.balance = balance + promo_price 
        else:
            self.balance = balance
        self.name = name
        self.acct_number = acct_number
        self.isFrozen = False
        self.isAdmin = isAdmin

    def deposit(self, amount):
        if not self.isFrozen:
            self.balance += amount
        else:
            return "Can't Deposit, Account is frozen"

    def withdraw(self, amount):
        if not self.isFrozen:
            if amount <= self.balance:
                self.balance -= amount
                return "Success"
            else:
                return "Insufficient Funds"
        else:
            return "Can't Withdraw, Account is frozen"

    def transfer(self, amount, recipient):
        if not self.isFrozen:
            tx = self.withdraw(amount)
            if tx == "Success":
                recipient.deposit(amount)
            else:
                return tx
        else:
            return "Can't Transfer, Account is frozen"

    def freeze(self, account):
        if self.isAdmin:
            if not self.isFrozen:
                self.isFrozen = True
                return f"{account.name} is frozen"
            else:
                return "Account is already frozen"
        else:
            return "Cannot perform this action, require admin privilege"

# freeze(account)
#unfree (account)
#Admin True
#isAdmin = False
#isFreezed = False
joy = BankAccount('Joy', 5000, True)
tom = BankAccount('Tom', 0)

print(joy.freeze(tom))
print(tom.freeze(joy))

print(joy.transfer(1000, tom))
