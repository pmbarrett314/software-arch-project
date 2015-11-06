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
import account

class Transaction(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    time = DateField()
    value = DoubleField()
    to_account = ForeignKeyField(account.Account, related_name='to_transactions')
    from_account = ForeignKeyField(account.Account, related_name='from_transactions')

    #def __init__(self, log_content="", start=None, end=None):
    #    return None

    def __str__(self):
        return "%s: %s transferred from %s to %s" % (time, value, from_account, to_account)
        