import os
import sys
import warnings
import getpass
import user as User
import customer as Customer
import admin as Admin
import account as Account
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
        try:
            user = User.login(username, passwd)
        except:
            user = ""
            printf "Error:  Login failed"
        return user



    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer():
        username = input("Enter username: ")
        passwd = getpass.getpass()
        try:
            Admin.create_customer(username, passwd)
            print "Customer created successfully"
        except:
            print "Error creating new customer"
        return

    def assignAccount():
        account = input("Account number: ")
        user = input("User ID #: ")
        try:
            Admin.assign_account(account, user)
            print "Account assignment successful\n"
        except:
            print "Error in account assignment\n"
        return

    def accountInfo():
        account_array = Admin.get_all_account_info()
        for account in account_array:
            print account
        return

    def systemLog():
        system_log = Admin.get_system_log()
        for item in system_log:
            print item
        return

    def createAccount():
        account_type = input("Checking or Savings account (c/s): ")
        if account_type.lower == "c":
            acct_type = "checking"
        elif account_type.lower == "s":
            acct_type = "savings"
        else:
            print "Invalid Account type.  Try again."
            return None
        try:
            createAccount(acct_type)
            print "Account created"
        except:
            print "Error creating account"

        return None

    def suspendAccount():
        try:
            customer_id = input("Customer ID: ")
            #get customer object from customer_id
            Admin.suspend_customer(customer)
            print "Customer suspended.\n"
        except:
            print "Problem suspending customer.  Try again.\n"

        return None

    def activateAccount():
        try:
            customer_id = input("Customer ID: ")
            #get customer object from customer_id
            Admin.activate_customer(customer)
            print "Customer activated.\n"
        except:
            print "Problem activating customer.  Try again.\n"

        return None

    #############################
    ### CUSTOMER FUNCTIONS - MAIN
    #############################

    def deposit():
        return

    def withdraw():
        return

    def transfer():
        return

    def customerLog():
        return
