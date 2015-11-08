'''
Created Nov 5 2015

Project:  

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

###Use models.py###

import os
import sys
import sqlite3
import warnings

from db_config import *
import user

class Customer(user.User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Customer")
    active = BooleanField(default=True)

    def login(username, password):
        '''
        If the Customer with the given password exists, return it
        '''
        return Customer.get(username=username, password=password)

    def deposit(self, acct, amount):
        '''
        Deposit the given amount into the specified account if the user owns that account.
        '''
        #Make sure the user owns the account
        if acct.owner == self:
            #Deposit the Money
            acct.deposit(amount)

        else:
            print("Deposit Fail")
            #raise Exception

    def withdraw(self, acct, amount):
        '''
        Withdraw money from the given account
        '''
        #Make sure the user owns the account
        if acct.owner == self:
            acct.withdraw(amount)
            #transaction.Transaction.create_withdraw_log(self, amount, account)

        else:
            print("Withdraw Fail")
            #raise Exception

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit 
        it in the destination account if the user owns both accounts
        '''
        if sourceAccount.owner == self:
            sourceAccount.send_transfer(amount, destinationAccount)
        else:
            pass
        #Withrdraw money from source account.
        #self.withdraw(sourceAccount, amount)
        #self.deposit(destinationAccount, amount)
        #transaction.Transaction.create_transfer_log(self, amount, destinationAccount, sourceAccount)

    def get_customer_log(self):
        '''
        Returns the transaction log relating to the Customer
        '''
        return self.transactions