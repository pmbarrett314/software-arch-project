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

from class_lib.db_config import *
from peewee import *

class User(DatabaseModel):

    username = CharField(unique=True)
    password = CharField()
    user_type = CharField()

    def __str__(self):
        return "%s (%s)" % (self.username, self.user_type)