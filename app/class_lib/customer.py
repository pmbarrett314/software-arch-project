'''
Created Nov 5 2015

Project:  

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import os
import sys
import sqlite3
import warnings
from db_config import *
from user import User


class Customer(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Customer")
    active = BooleanField(default=True)
    #def __init__(self, accounts = [], active = false):
    #    return None

    def __str__(self):
        return self.username

    def deposit(self, account, amount):
        #Make sure the user owns the account
        if account.owner == self:
            #Deposit the Money
            account.deposit(amount)
            
        else:
            raise Exception


    def withdraw(self, account, amount):
        '''
        Withdraw money from the given account
        '''
        #Make sure the user owns the account
        if account.owner == self:
            account.withdraw(amount)
        else:
            pass
            #raise Exception

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit 
        it in the destination account
        '''
        #Withrdraw money from source account.
        self.withdraw(sourceAccount, amount)
        destinationAccount.deposit(amount)

    def get_customer_log():
        return  