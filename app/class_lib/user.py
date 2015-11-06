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
from peewee import *

class User(DatabaseModel):

	username = CharField(unique=True)
	password = CharField()
	user_type = CharField()

    #def login(username, password):
    #	return user

    #def logout():
    #    return

    
