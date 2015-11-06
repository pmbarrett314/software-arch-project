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

class Customer(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################
    
    user_info = ForeignKeyField(User, related_name="customer_info")
    
    #def __init__(self, accounts = [], active = false):
    #    return None

    def deposit(Account, amount):
        return

    def withdraw(Account, amount):
        return

    def transfer(sourceAccount, destinationAccount, amount):
        return

    def get_customer_log():
        return log