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
import class_lib.account  as account
import class_lib.customer as customer

class Savings_Account(account.Account):

	############################
    ###  Class Variables
    ############################
    owner = ForeignKeyField(customer.Customer, related_name='savings_accounts', null=True)
    account_type = CharField(default="Savings")

    @staticmethod
    def get_account(account_number):
        '''
        Returns an account with the given account number.
        Takes a string as a parameter
        '''
        return Savings_Account.get(account_number=account_number)
