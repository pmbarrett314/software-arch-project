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
import class_lib.account as account
import class_lib.customer as customer

class Checking_Account(account.Account):
    owner = ForeignKeyField(customer.Customer, related_name='checking_accounts', null=True)
    account_type = CharField(default="Checking")

