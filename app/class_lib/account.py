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
from db_config import *
from customer import Customer
class Account(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    account_number = IntegerField()
    balance = DoubleField()
    account_type = CharField()

    owner = ForeignKeyField(Customer, related_name="accounts")


    #def __init__(self, account_number = 0, balance = 0.00, type = ''):
    #    return None

    def current_balance():
        return None
    
    def deposit(depositAmount):
        return None

    def withdraw(withdrawAmount):
        return None
