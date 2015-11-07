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
from account import Account
from customer import Customer

class Checking_Account(Account):
    owner = ForeignKeyField(Customer, related_name='checking_accounts', null=True)
    account_type = CharField(default="Checking")

