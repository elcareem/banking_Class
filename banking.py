import random

class BankAccount:
    def __init__(self, name, balance):
        promo_price = 2000
        acct_number = int(random.random() * 10000000000)
          
        if random.random() < 0.5:
            self.promo = True
        else:
            self.promo = False

        if self.promo:
            self.balance = balance + promo_price 
        else:
            self.balance = balance
        self.name = name
        self.acct_number = acct_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return "Success"
        else:
            return "Insufficient Funds"

    def transfer(self, amount, recipient):
        tx = self.withdraw(amount)
        if tx == "Success":
            recipient.deposit(amount)
        else:
            return tx


joy = BankAccount('Joy', 5000)
tom = BankAccount('Tom', 0)

print(joy.balance, joy.promo)
joy.deposit(1000)
print(joy.balance)
joy.withdraw(200)
print(joy.balance)

joy.transfer(1000, tom)

print(tom.balance, tom.promo)

