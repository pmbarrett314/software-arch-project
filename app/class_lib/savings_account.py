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
import account 
import customer

class Savings_Account(account.Account):
    owner = ForeignKeyField(customer.Customer, related_name='savings_accounts', null=True)
    account_type = CharField(default="Savings")