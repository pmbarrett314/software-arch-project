'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import model.checking_account as checking_account
import model.customer as customer
import model.savings_account as savings_account
import model.transaction as transaction
import model.user as user

from db.db_config import *


class Admin(user.User):
    ############################
    ###  Class Variables
    ############################
    user_type = CharField(default="Admin")

    @staticmethod
    def login(username, password):
        '''
        If the Admin with the given password exists, return it
        Takes two strings as parameters
        '''
        return Admin.get(username=username, password=password)

    def create_customer(self, username, password):
        '''
        Creates a new customer object and returns it
        Takes two strings as parameters
        '''
        if len(password) < 8:
            raise Exception("Password is too short")
        user_name_exists = False
        try:
            Admin.get(usemodelrname=username)
            user_name_exists = True
        except:
            pass
        if user_name_exists:
            raise Exception("Username is already in use")
        cust = customer.Customer(username=username, password=password)
        cust.save()
        return cust

    def assign_account(self, acct, customer):
        '''
        Assign an account to a customer
        Takes an account object and a customer object as parameters
        '''
        acct.owner = customer
        acct.save()

    def get_all_account_info(self):
        '''
        Retrieves infomration about all of the accounts as an array of accounts
        '''
        # Create the accounts array
        accounts = []
        # Add savings accounts to the accounts array
        for each_account in savings_account.Savings_Account.select():
            accounts.append(str(each_account))
        # Add Checking accounts to the accounts array
        for each_account in checking_account.Checking_Account.select():
            accounts.append(str(each_account))
        # Return the accounts array
        return accounts

    def get_all_customers(self):
        '''
        Retrieves information about all of the Customers as an array of Customers
        '''
        customer_array = []
        for each_customer in customer.Customer.select():
            customer_array.append(each_customer)
        return customer_array

    def get_system_log(self):
        '''
        Retrieves all of the transactions from the system
        '''
        return transaction.Transaction.select()

    def suspend_customer(self, customer):
        '''
        Make the Customer Inactive
        Takes a customer object as a parameter
        '''
        customer.active = False
        customer.save()

    def activate_customer(self, customer):
        '''
        Make the Cusomter Active
        Takes a customer object as a parameter
        '''
        customer.active = True
        customer.save()

    def create_account(self, account_type, account_number):
        '''
        Creates and returns a new account object with the given account type and account number
        Takes two strings as parameters
        '''
        # Try to retrieve an account with the same account number and, if it succeeds, we know
        # that number is already in use.
        account_number_exists = False
        try:
            checking_account.Checking_Account.get(account_number=account_number)
            account_number_exists = True
        except:
            try:
                savings_account.Savings_Account.get(account_number=account_number)
                account_number_exists = True
            except:
                pass
        # Throw exception if account number is already in use
        if account_number_exists:
            raise Exception("Account Number is already in use")
        # Create a checking account if that's the account type
        if account_type == "checking":
            acct = checking_account.Checking_Account(account_number=account_number).save()
        # Create a savings account if that's the account type
        elif account_type == "savings":
            acct = savings_account.Savings_Account(account_number=account_number).save()
        # If we don't have a matching account type, raise an exception
        else:
            raise Exception("Invalid Account Type")
        return acct
