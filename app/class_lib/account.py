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
        Takes a double as a parameter
        '''
        #Update the account's balance
        self.balance += depositAmount
        self.save()
        #Create a transaction log for the deposit
        transaction.Transaction.create_deposit_log(self.owner, depositAmount, self)

    def withdraw(self, withdrawAmount):
        '''
        Withdraw money from the account
        Takes a double as a parameter
        '''
        #Make sure the account has enough money
        if withdrawAmount <= self.balance:
            #Update the account's balance
            self.balance -= withdrawAmount
            self.save()
            #Create the transaction log for the withdrawl
            transaction.Transaction.create_withdrawl_log(self.owner, withdrawAmount, self)

        else:
            raise Exception("Insufficient Funds.")

    def send_transfer(self, transferAmount, destinationAccount):
        '''
        The account sends a transfer to another account. 
        Make sure there's enough money and remove it then record the transaction
        Takes a double and another account object as parameters
        '''
        #Make sure the account has enough money
        if transferAmount <= self.balance:
            #Update the account's balance 
            self.balance -= transferAmount
            self.save()
            #Deliver money to other account
            destinationAccount.receive_trasfer(transferAmount, self)
            #Create the transaction log for the tarnsfer
            transaction.Transaction.create_transfer_sent_log(self.owner, transferAmount, self, destinationAccount)
        else:
            raise Exception("Insufficient Funds for Transfer.")

    def receive_trasfer(self, transferAmount, sourceAccount):
        '''
        The account receives a transfer from another account. 
        Add the money and record the transaction
        Takes a double and another account object as parameters
        '''
        #Update account's balance
        self.balance += transferAmount
        self.save()
        #Create the transaction log for receiving the transfer
        transaction.Transaction.create_transfer_received_log(self.owner, transferAmount, sourceAccount, self)

    @staticmethod
    def get_account(account_number):
        '''
        Returns an account with the given account number.
        Takes a string as a parameter
        Should be overridden by subclasses
        '''
        return Account.get(account_number=account_number)
            





