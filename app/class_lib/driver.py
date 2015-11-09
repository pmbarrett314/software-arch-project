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
        user = None
        while user == None:
            username = input("Username: ")
            password = getpass.getpass()
            try: 
                user = admin.Admin.login(username, password)
            except:
                pass
            try:
                user = customer.Customer.login(username, password)
            except:
                print("Invalid Login")
        return user

    def get_account():
        '''
        Ask the user for an account number, and return a valid account
        '''
        acct = None
        while acct == None:
            account_number = input("Account Number: ")
            try: 
                return savings_account.Savings_Account.get_account(account_number)
            except:
                pass
            try: 
                return checking_account.Checking_Account.get_account(account_number)
            except:
                pass
            print("Account not found")

    def get_amount():
        '''
        Ask the user for a valid amount to deposit, withdraw, or transfer
        '''
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

    def get_customer():
        '''
        Ask the user for a username and return the customer with that sername
        '''
        cust = None
        while cust == None:
            try:
                cust = customer.Customer.get_customer(input("Username: "))
            except:
                print("Could not find the customer with that username")
        return cust

    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer(user):
        username = input("Enter username: ")
        passwd = getpass.getpass()
        try:
            user.create_customer(username, passwd)
            print("Customer created successfully")
        except:
            print("Error creating new customer")
        return

    def assignAccount(user):
        account = BankSystemDriver.get_account()
        #get customer object from username
        cust = BankSystemDriver.get_customer()
        try:
            user.assign_account(account, cust)
            print("Account assignment successful\n")
        except Exception as e:
            print("Error in account assignment. %s\n" % e)
        return

    def accountInfo(user):
        account_array = user.get_all_account_info()
        for account in account_array:
            print(account)
        return

    def systemLog(user):
        system_log = admin.Admin.get_system_log()
        for item in system_log:
            print(item)
        return

    def createAccount(user):
        account_type = input("Checking or Savings account (c/s): ")
        if account_type.lower() == "c":
            acct_type = "checking"
        elif account_type.lower() == "s":
            acct_type = "savings"
        else:
            print("Invalid Account type.  Try again.")
            return None
        account_number = input("Account Number: ")
        try:
            user.create_account(acct_type, account_number)
            print("Account %s created" % account_number)
        except Exception as e:
            print("Error creating account. %s" % e)

        return None

    def suspendAccount(user):
        try:
            #get customer object from username
            cust = BankSystemDriver.get_customer()
            user.suspend_customer(cust)
            print("Customer suspended.\n")
        except:
            print("Problem suspending customer.  Try again.\n")

        return None

    def activateAccount(user):
        try:
            #get customer object from username
            cust = BankSystemDriver.get_customer()
            
            user.activate_customer(cust)
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






