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
from user import User
from transaction import Transaction
class Customer(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Customer")
    active = BooleanField(default=True)
    def login(username, password):
        return Customer.get(username=username, password=password)


    def deposit(self, account, amount):
        #Make sure the user owns the account
        if account.owner == self:
            #Deposit the Money
            account.deposit(amount)
            transactionDetails = "Deposited %s into %s leaving %s in the account." % (amount, account.account_number, account.current_balance())
            new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
            new_transaction.save()
        else:
            print("Deposit Fail")
            #raise Exception


    def withdraw(self, account, amount):
        '''
        Withdraw money from the given account
        '''
        #Make sure the user owns the account
        if account.owner == self:
            account.withdraw(amount)
            transactionDetails = "Withdrew %s from %s leaving %s in the account." % (amount, account.account_number, account.current_balance())
            new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
            new_transaction.save()
        else:
            print("Withdraw Fail")
            #raise Exception

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit 
        it in the destination account
        '''
        #Withrdraw money from source account.
        self.withdraw(sourceAccount, amount)
        self.deposit(destinationAccount, amount)
        transactionDetails = "Transferred %s from %s to %s. New Balances: %s (%s); %s (%s)" % (amount, sourceAccount.account_number, destinationAccount.account_number, sourceAccount.account_number, sourceAccount.current_balance(), destinationAccount.account_number, destinationAccount.current_balance())
        new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
        new_transaction.save()
    def get_customer_log(self):
        return self.transactions