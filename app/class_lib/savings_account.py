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
from account import Account
from customer import Customer

class Savings_Account(Account):
	owner = ForeignKeyField(Customer, related_name='savings_accounts')
   

    ############################
    ###  Initialize class object
    ############################

    #def __init__(self):
    #    return None
