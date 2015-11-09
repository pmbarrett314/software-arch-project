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

from class_lib.db_config import *

import class_lib.user as user
import class_lib.customer as customer
import class_lib.transaction as transaction
import class_lib.savings_account as savings_account
import class_lib.checking_account as checking_account

class Admin(user.User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Admin")

    def login(username, password):
        '''
        If the Admin with the given password exists, return it
        '''
        return Admin.get(username=username, password=password)

    def create_customer(self, username, password):
        '''
        Creates a new customer object
        '''
        cust = customer.Customer(username=username, password=password)
        cust.save()
        return customer

    def assign_account(self, acct, customer):
        '''
        Assign an account to a customer
        '''
        acct.owner = customer
        acct.save()

    def get_all_account_info(self):
        '''
        Retrieves infomration about all of the accounts as an array of strings
        '''
        accounts = []
        for each_account in savings_account.Savings_Account.select():
            accounts.append(str(each_account))
        for each_account in checking_account.Checking_Account.select():
            accounts.append(str(each_account))
        return accounts

    def get_system_log(self):
        '''
        Retrieves all of the transactions from the system
        '''
        return transaction.Transaction.select()

    def suspend_customer(self, customer):
        '''
        Make the Customer Inactive
        '''
        customer.active = False
        customer.save()

    def activate_customer(self, customer):
        '''
        Make the Cusomter Active
        '''
        customer.active = True
        customer.save()