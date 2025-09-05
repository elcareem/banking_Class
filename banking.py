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

        self.name = name
        self.acct_number = acct_number
        self.balance = balance

joy = BankAccount('Joy', 1000)

print(joy.balance, joy.promo)
