"""
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Bank_account():

    def __init__(self,a,b = 0):
        self.attributes = a
        self.balance = b

    def deposit(self,d):
        self.balance += d
        print('Deposit Accepted')

    def withdraw(self,w):
        if self.balance >= w:
            self.balance -= w
            print('Withdrawal Accepted')
        else:
            print('Insufficient funds!')


oper = Bank_account(input(),int(input()))

oper.deposit(int(input()))

oper.withdraw(int(input()))
