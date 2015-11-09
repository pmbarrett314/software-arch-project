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
from peewee import *

from class_lib.db_config import *
import class_lib.customer as customer
import class_lib.transaction as transaction

class Account(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################
    account_number = CharField(unique=True)
    balance = DoubleField(default=0.0)
    account_type = CharField()
    owner = ForeignKeyField(customer.Customer, related_name="accounts", null=True)

    def __str__(self):
        #return self.account_number
        return "Account Number: %s; Owner: %s; (%s Account): $%s" % (self.account_number, self.owner, self.account_type, self.balance)

    def current_balance(self):
        '''
        Get the current balance of the account
        '''
        return self.balance
    
    def deposit(self, depositAmount):
        '''
        Deposit money into the account
        '''
        self.balance += depositAmount
        self.save()
        transaction.Transaction.create_deposit_log(self.owner, depositAmount, self)

    def withdraw(self, withdrawAmount):
        '''
        Withdraw money from the account
        '''
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount
            self.save()
            transaction.Transaction.create_withdrawl_log(self.owner, withdrawAmount, self)

        else:
            raise Exception("There is not enough money in the account")

    def send_transfer(self, transferAmount, destinationAccount):
        '''
        '''
        if transferAmount <= self.balance:
            self.balance -= transferAmount
            destinationAccount.receive_trasfer(transferAmount, self)
            self.save()
            transaction.Transaction.create_transfer_sent_log(self.owner, transferAmount, self, destinationAccount)
        else:
            raise Exception("Insufficient Funds for Transfer")

    def receive_trasfer(self, transferAmount, sourceAccount):
        '''
        '''
        self.balance += transferAmount
        self.save()
        transaction.Transaction.create_transfer_received_log(self.owner, transferAmount, sourceAccount, self)

'''
    def get_account(account_number):
   
        Returns an account with the given account number.
   
        try:
            return Account.get(account_number=account_number)
        except:
            raise Exception("Account not found")
            '''