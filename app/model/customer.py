'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import model.user as user

from db.db_config import *


class Customer(user.User):
    ############################
    ###  Class Variables
    ############################
    user_type = CharField(default="Customer")
    active = BooleanField(default=True)

    @staticmethod
    def login(username, password):
        '''
        If the Customer with the given password exists, return it
        Takes two strings as parameters
        '''
        return Customer.get(username=username, password=password, active=True)

    def deposit(self, acct, amount):
        '''
        Deposit the given amount into the specified account if the user owns that account.
        Takes in one account object and a double
        '''
        # Make sure the user owns the account
        if acct.owner == self:
            # Deposit the Money
            acct.deposit(amount)

        else:
            raise Exception("User does not own that account")

    def withdraw(self, acct, amount):
        '''
        Withdraw money from the given account
        Takes in one account object and a double
        '''
        # Make sure the user owns the account
        if acct.owner == self:
            # Withdraw the money
            acct.withdraw(amount)

        else:
            raise Exception("User does not own that account")

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit
        it in the destination account if the user owns both accounts
        Takes in two account objects and a double
        '''
        # Make sure the user owns the account they are transfering from
        if sourceAccount.owner == self:
            # Transfer the money
            sourceAccount.send_transfer(amount, destinationAccount)
        else:
            raise Exception("User does not own that account")

    def get_customer_log(self):
        '''
        Returns the transaction log relating to the Customer
        '''
        return self.transactions

    @staticmethod
    def get_customer(username):
        '''
        Returns the customer with the given username
        '''
        return Customer.get(username=username)
