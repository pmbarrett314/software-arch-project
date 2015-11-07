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
import datetime

class Transaction(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    time = DateField(default=datetime.datetime.now)
    owner = ForeignKeyField(Customer, related_name='transactions')
    details = CharField()
    
    #def __init__(self, log_content="", start=None, end=None):
    #    return None

    def __str__(self):
        return "%s: (%s) %s" % (self.time, self.owner, self.details)