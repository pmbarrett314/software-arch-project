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
import customer
import datetime

class Transaction(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################
    time = DateField(default=datetime.datetime.now)
    owner = ForeignKeyField(customer.Customer, related_name='transactions')
    details = CharField()

    def __str__(self):
        return "%s: (%s) %s" % (self.time, self.owner, self.details)
        
    def create_withdrawl_log(customer, amount, account):
        '''
        Returns the log for a withdrawl by the given user for the amount and from
        the specified account
        '''
        content = "%s: $%s withdrawn. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    def create_deposit_log(customer, amount, account):
        '''
        Returns the log for a deposited by the given user for the amount and into
        the specified account
        '''
        content = "%s: $%s deposited. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    def create_transfer_sent_log(customer, amount, sourceAccount, destinationAccount):
        '''
        Returns the log for a transfer by the given user for the amount and from
        from_account and into to_account
        '''
        content = "%s: $%s trasfered to %s. New Balance: $%s " % (sourceAccount.account_number, amount, destinationAccount.account_number, 
                                                                sourceAccount.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    def create_transfer_received_log(customer, amount, sourceAccount, destinationAccount):
        '''
        Returns the log for a transfer by the given user for the amount and from
        from_account and into to_account
        '''
        content = "%s: $%s trasfered from %s. New Balance: $%s " % (destinationAccount.account_number, amount, sourceAccount.account_number, 
                                                                destinationAccount.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()