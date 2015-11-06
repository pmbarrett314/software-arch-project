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

class Log(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    time = DateField()
    value = DoubleField()
    to_account = ForeignKeyField(Account, related_name='to_transactions')
    from_account = ForeignKeyField(Account, related_name='from_transactions')

    #def __init__(self, log_content="", start=None, end=None):
    #    return None

    def print_log():
        return None
