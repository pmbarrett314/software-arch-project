import os
import sys
import warnings
import getpass
import class_lib.user as user
import class_lib.customer as customer
import class_lib.admin as admin
import class_lib.savings_account as savings_account
import class_lib.checking_account as checking_account
from class_lib.account import Account

#import other classes

class BankSystemDriver():

    def __init__():
        return



    #############################
    ### COMMON USER FUNCTIONS
    #############################

    def login():
        username = input("Username: ")
        passwd = getpass.getpass()
        user = User.login(username, passwd)
        return user

    def get_account():
        acct = None
        while acct == None:
            account_number = input("Account Number: ")
            try: 
                return savings_account.Savings_Account.get(account_number=account_number)
            except:
                pass
            try: 
                return checking_account.Checking_Account.get(account_number=account_number)
            except:
                pass
            print("Account not found")

    def get_amount():
        amount = None
        while amount == None:
            try:
                amount = float(input("Enter Amount: $"))
            except: 
                print("Invalid Amount")
        return amount
    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer():
        return

    def assignAccount():
        account = input("Account number: ")
        user = input("User ID #: ")
        #command for assigning account
        return

    def accountInfo():
        
        account = input("Account number to fetch: ")
        #command for getting account info
        return

    def systemLog():
        #command for getting system log
        return

    def createAccount():
        return

    def suspendAccount():
        account = input("Account number to suspend: ")
        try:
            #suspend account command
            pass
        except:
            print("Problem suspending account.  Try again.")

        return None

    #############################
    ### CUSTOMER FUNCTIONS - MAIN
    #############################

    def deposit(user):
        acct = BankSystemDriver.get_account()
        amount = BankSystemDriver.get_amount()
        try:
            user.deposit(acct, amount)
        except:
            print("Could not make a deposit into %s" % acct.account_number)
        return

    def withdraw():
        acct = BankSystemDriver.get_account()
        amount = BankSystemDriver.get_amount()
        try:
            user.deposit(acct, amount)
        except:
            print("Could not make a withdrawl from %s" % acct.account_number)
        return

    def transfer():
        return

    def customerLog():
        return
