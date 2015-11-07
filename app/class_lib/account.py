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
from db_config import *
from customer import Customer

class Account(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    account_number = CharField(unique=True)
    balance = DoubleField(default=0.0)
    account_type = CharField()

    owner = ForeignKeyField(Customer, related_name="accounts", null=True)


    #def __init__(self, account_number = 0, balance = 0.00, type = ''):
    #    return None

    def __str__(self):
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

    def withdraw(self, withdrawAmount):
        '''
        Withdraw money from the account
        '''
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount
            self.save()

        else:
            pass#throw Exception