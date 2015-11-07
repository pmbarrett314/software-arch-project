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
from customer import Customer
from transaction import Transaction

class Admin(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Admin")
    #def __init__(self):
    #    return None

    def login(username, password):
        return Admin.get(username=username, password=password)

    def create_customer(self, username, password):
        '''
        Creates a new customer object
        '''
        customer = Customer(username=username, password=password)
        customer.save()
        return customer

    def assign_account(self, account, customer):
        '''
        Assign an account to a customer
        '''
        account.owner = customer
        account.save()

    def get_all_account_info(self):
        '''
        Retrieves infomration about all of the accounts as an array of strings
        '''
        accounts = []
        for each_account in Savings_Account.select():
            accounts.append(str(each_account))
        for each_account in Checking_Account.select():
            accounts.append(str(each_account))
        return accounts

    def get_system_log(self):
        '''
        Retrieves all of the transactions from the system
        '''
        return Transaction.select()

    #def create_bank_account(self):
    #    return account

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