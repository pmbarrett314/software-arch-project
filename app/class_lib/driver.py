import os
import sys
import warnings
import getpass
import class_lib.customer as customer
import class_lib.admin as admin
import class_lib.savings_account as savings_account
import class_lib.checking_account as checking_account

#import other classes

class BankSystemDriver():

    __instance = None

    def __init__(self):
        self.user = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance=cls()
        return cls.__instance

    #############################
    ### COMMON USER FUNCTIONS
    #############################

    def login(self):
        '''
        Request user credentials and logs them in as either an Admin or Customer
        '''
        self.user = None
        while self.user is None:
            username = input("Username: ")
            password = getpass.getpass()
            try:
                self.user = admin.Admin.login(username, password)
            except admin.Admin.DoesNotExist:
                try:
                    self.user = customer.Customer.login(username, password)
                except customer.Customer.DoesNotExist:
                    print("Invalid Login")

    def get_account(self):
        '''
        Ask the user for an account number, and return a valid account
        '''
        acct = None
        while acct is None:
            account_number = input("Account Number: ")
            try:
                return savings_account.Savings_Account.get_account(account_number)
            except savings_account.Savings_Account.DoesNotExist:
                try:
                    return checking_account.Checking_Account.get_account(account_number)
                except checking_account.Checking_Account.DoesNotExist:
                    print("Account not found")

    def get_amount(self):
        '''
        Ask the user for a valid amount to deposit, withdraw, or transfer
        '''
        amount = None
        while amount is None:
            try:
                amount = float(input("Enter Amount: $"))
                if amount < 0:
                    amount = None
                    print("Invalid Amount, amount must be positive")
            except ValueError:
                print("Invalid Amount, amount must be a positive number")
        return amount

    def get_customer(self):
        '''
        Ask the user for a username and return the customer with that username
        '''
        cust = None
        while cust is None:
            try:
                cust = customer.Customer.get_customer(input("Username: "))
            except customer.Customer.DoesNotExist:
                print("Could not find the customer with that username")
        return cust

    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def newCustomer(self):
        username = input("Enter username: ")
        passwd = getpass.getpass()
        try:
            self.user.create_customer(username, passwd)
            print("Customer created successfully")
        except:
            print("Error creating new customer")
        return

    def assignAccount(self):
        account = self.get_account()
        #get customer object from username
        cust = self.get_customer()
        try:
            self.user.assign_account(account, cust)
            print("Account assignment successful\n")
        except Exception as e:
            print("Error in account assignment. %s\n" % e)
        return

    def accountInfo(self):
        account_array = self.user.get_all_account_info()
        for account in account_array:
            print(account)
        return

    def systemLog(self):
        system_log = self.user.get_system_log()
        for item in system_log:
            print(item)
        return

    def createAccount(self):
        account_type = input("Checking or Savings account (c/s): ")
        if account_type.lower() == "c":
            acct_type = "checking"
        elif account_type.lower() == "s":
            acct_type = "savings"
        else:
            print("Invalid Account type.  Try again.")
            return
        account_number = input("Account Number: ")
        try:
            self.user.create_account(acct_type, account_number)
            print("Account %s created" % account_number)
        except Exception as e:
            print("Error creating account. %s" % e)

    def suspendAccount(self):
        try:
            # get customer object from username
            cust = self.get_customer()
            self.user.suspend_customer(cust)
            print("Customer suspended.\n")
        except:
            print("Problem suspending customer.  Try again.\n")

    def activateAccount(self):
        try:
            # get customer object from username
            cust = self.get_customer()

            self.user.activate_customer(cust)
            print("Customer activated.\n")
        except:
            print("Problem suspending account.  Try again.")

    #############################
    ### CUSTOMER FUNCTIONS - MAIN
    #############################

    def deposit(self):
        acct = self.get_account()
        amount = self.get_amount()
        try:
            self.user.deposit(acct, amount)
            print("$%s deposited into %s." % (amount, acct.account_number))
        except Exception as e:
            print("Could not make a deposit into %s. %s" % (acct.account_number, e))
        return

    def withdraw(self):
        acct = self.get_account()
        amount = self.get_amount()
        try:
            self.user.withdraw(acct, amount)
            print("$%s withdrawn from %s." % (amount, acct.account_number))
        except Exception as e:
            print("Could not make a withdrawl from %s. %s" % (acct.account_number, e))
        return

    def transfer(self):

        print("Which account would you like to transfer from?")
        source_acccount = self.get_account()
        print("How much would you like to transfer?")
        amount = self.get_amount()
        print("Which account would you like to transfer to?")
        destination_account = self.get_account()
        try:
            self.user.transfer(source_acccount, destination_account, amount)
            print("$%s trasferred from %s." % (amount, source_acccount.account_number))
        except Exception as e:
            print("Could not make the transfer from %s. %s" % (source_acccount.account_number, e))
        return

    def customerLog(self):
        for each_log in self.user.get_customer_log():
            print(each_log)
        return






