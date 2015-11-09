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
        user = User.login(username, passwd)
        return user



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
            print "Problem suspending account.  Try again."

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
