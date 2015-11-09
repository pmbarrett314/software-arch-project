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
        try:
            user = User.login(username, passwd)
        except:
            user = ""
            print("Error:  Login failed")
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
                if amount < 0:
                    amount = None
                    print("Invalid Amount")
            except: 
                print("Invalid Amount")
        return amount

    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer():
        username = input("Enter username: ")
        passwd = getpass.getpass()
        try:
            Admin.create_customer(username, passwd)
            print("Customer created successfully")
        except:
            print("Error creating new customer")
        return

    def assignAccount():
        account = input("Account number: ")
        user = input("User ID #: ")
        try:
            Admin.assign_account(account, user)
            print("Account assignment successful\n")
        except:
            print("Error in account assignment\n")
        return

    def accountInfo():
        account_array = Admin.get_all_account_info()
        for account in account_array:
            print(account)
        return

    def systemLog():
        system_log = Admin.get_system_log()
        for item in system_log:
            print(item)
        return

    def createAccount():
        account_type = input("Checking or Savings account (c/s): ")
        if account_type.lower == "c":
            acct_type = "checking"
        elif account_type.lower == "s":
            acct_type = "savings"
        else:
            print("Invalid Account type.  Try again.")
            return None
        try:
            createAccount(acct_type)
            print("Account created")
        except:
            print("Error creating account")

        return None

    def suspendAccount():
        try:
            customer_id = input("Customer ID: ")
            #get customer object from customer_id
            Admin.suspend_customer(customer)
            print("Customer suspended.\n")
        except:
            print("Problem suspending customer.  Try again.\n")

        return None

    def activateAccount():
        try:
            customer_id = input("Customer ID: ")
            #get customer object from customer_id
            Admin.activate_customer(customer)
            print("Customer activated.\n")
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
            print("$%s deposited into %s." % (amount, acct.account_number))
        except Exception as e:
            print("Could not make a deposit into %s. %s" % (acct.account_number, e))
        return

    def withdraw(user):
        acct = BankSystemDriver.get_account()
        amount = BankSystemDriver.get_amount()
        try:
            user.withdraw(acct, amount)
            print("$%s withdrawn from %s." % (amount, acct.account_number))
        except Exception as e:
            print("Could not make a withdrawl from %s. %s" % (acct.account_number, e))
        return

    def transfer(user):

        print("Which account would you like to transfer from?")
        source_acccount = BankSystemDriver.get_account()
        print("How much would you like to transfer?")
        amount = BankSystemDriver.get_amount()
        print("Which account would you like to transfer to?")
        destination_account = BankSystemDriver.get_account()
        try:
            user.transfer(source_acccount, destination_account, amount)
            print("$%s trasferred from %s." % (amount, source_acccount.account_number))
        except Exception as e:
            print("Could not make the transfer from %s. %s" % (source_acccount.account_number, e))
        return

    def customerLog(user):
        for each_log in user.get_customer_log():
            print(each_log)
        return






