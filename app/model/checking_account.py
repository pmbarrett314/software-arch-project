'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import model.account as account
import model.customer as customer

from db.db_config import *


class Checking_Account(account.Account):
    ############################
    ###  Class Variables
    ############################
    owner = ForeignKeyField(customer.Customer, related_name='checking_accounts', null=True)
    account_type = CharField(default="Checking")

    @staticmethod
    def get_account(account_number):
        '''
        Returns an account with the given account number.
        Takes a string as a parameter
        '''
        return Checking_Account.get(account_number=account_number)
