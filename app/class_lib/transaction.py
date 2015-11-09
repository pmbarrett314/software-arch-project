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

from class_lib.db_config import *
import class_lib.customer as customer
import datetime

class Transaction(DatabaseModel):

    ############################
    ###  Class Variables
    ############################
    time = DateField(default=datetime.datetime.now)
    owner = ForeignKeyField(customer.Customer, related_name='transactions')
    details = CharField()

    def __str__(self):
        return "%s: (%s) %s" % (self.time, self.owner, self.details)
      

    @staticmethod
    def create_withdraw_log(customer, amount, account):
        '''
        Creates and saves the log for a withdraw by the given user for the amount and from
        the specified account
        '''
        content = "%s: $%s withdrawn. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    @staticmethod
    def create_deposit_log(customer, amount, account):
        '''
        Creates and saves the log for a deposited by the given user for the amount and into
        the specified account
        '''
        content = "%s: $%s deposited. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    @staticmethod
    def create_transfer_sent_log(customer, amount, sourceAccount, destinationAccount):
        '''
        Creates and saves the log for a transfer by the given user for the amount and from
        sourceAccount and into destinationAccount
        '''
        content = "%s: $%s trasfered to %s. New Balance: $%s " % (sourceAccount.account_number, amount, destinationAccount.account_number, 
                                                                sourceAccount.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    @staticmethod
    def create_transfer_received_log(customer, amount, sourceAccount, destinationAccount):
        '''
        Creates and saves the log for a transfer by the given user for the amount and from
        sourceAccount and into destinationAccount
        '''
        content = "%s: $%s trasfered from %s. New Balance: $%s " % (destinationAccount.account_number, amount, sourceAccount.account_number, 
                                                                destinationAccount.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()