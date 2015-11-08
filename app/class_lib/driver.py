import os
import sys
import warnings
import getpass
import user as User
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

        role = User.login(username, passwd)
        return role



    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer():
        return

    def assignAccount():
        return

    def accountInfo():
        return

    def systemLog():
        return

    def createAccount():
        return

    def suspendAccount():
        return

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
