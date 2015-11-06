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

class Admin(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################
    user_info = ForeignKeyField(User, related_name='admin_info')
    #def __init__(self):
    #    return None

    def create_customer(string):
        return customer

    def assign_account(Account, Customer):
        return

    def get_all_account_info():
        return

    def get_system_log():
        return log

    def create_bank_account():
        return account

    def suspend_account(account):
        return
