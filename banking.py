import random
from enum import Enum

class BankAccount:
    def __init__(self, name, balance, isAdmin = False, receiveMail = False, receiveSMS = False):
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
        self.receiveMail = receiveMail
        self.receiveSMS = receiveSMS

    def deposit(self, amount):
        if not self.isFrozen:
            self.balance += amount
            topUp = True
            self.message(amount, topUp)
            return "Success"
        else:
            return "Can't Deposit, Account is frozen"

    def withdraw(self, amount):
        if not self.isFrozen:
            if amount <= self.balance:
                self.balance -= amount
                topUp = False 
                self.message(amount, topUp)
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
                return "Transfer complete"
            else:
                return tx
        else:
            return "Can't Transfer, Account is frozen"

    def freeze(self, account):
        if self.isAdmin:
            if not account.isFrozen:
                account.isFrozen = True
                return f"{account.name}'s account is frozen"
            else:
                return "Account is already frozen"
        else:
            return "Cannot perform this action"

    def unfreeze(self, account):
        if self.isAdmin:
            if account.isFrozen:
                account.isFrozen = False
                return f"{account.name} is now unfrozen"
            else:
                return "Account is not frozen"
        else:
            return "Cannot perfom this action"
    
    def message(self, amount, topUp):
        
        if self.receiveMail:
            if topUp:
                print(f"""
                        MAIL: Credit
                        {self.name}, you have been credited N{amount}
                        Balance: {self.balance}
                      """)
            else:
                print(f"""
                        MAIL: Debit
                        {self.name}, you have been debited N{amount}
                        Balance: {self.balance}
                      """)

        if self.receiveSMS:
            if topUp:
                print(f"""
                        SMS: Credit
                        {self.name}, you have been credited N{amount}
                        Balance: {self.balance}
                      """)
            else:
                print(f"""
                        SMS: Debit
                        {self.name}, you have been debited N{amount}
                        Balance: {self.balance}
                      """)


joy = BankAccount("Joy", 5000, receiveSMS = True, receiveMail = True)
tom = BankAccount("Tom", 2000, receiveMail = True, receiveSMS = True)

joy.transfer(700, tom)
