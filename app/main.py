import os
import sys
import warnings
import traceback
from class_lib.driver import BankSystemDriver as driver
import class_lib.admin as admin
import class_lib.customer as customer

def login():
    username = input("Username: ")
    password = input("Password: ")
    try: 
      return admin.Admin.get(username=username, password=password)
    except:
      pass
    try:
      return customer.Customer.get(username=username, password=password)
    except:
      print("Invalid Login")
    role = "admin"
    return role

def getOptions(user):
    if(isinstance(user, admin.Admin)):
        getAdminOptions()
    elif(isinstance(user, customer.Customer)):
        getCustomerOptions(user)
    else:
        print("Login error: Account type invalid")
        return


def getAdminOptions():

    while 1:
    
        print("Enter option, for list of options enter 'help'")

        option = input()

        #print instructions for User Input
        if option.lower() == 'help':
            
            print("Valid Admin Commands:\n" + \
                  "=====================\n" + \
                  "\n" + \
                  "n     -New Customer\n" + \
                  "a     -Assign Account\n" + \
                  "i     -Info on Accounts\n" + \
                  "l     -Get System Log\n" + \
                  "c     -Create Account\n" + \
                  "s     -Suspend Account\n" + \
                  "r     -Reactivate/Activate Account\n" + \
                  "exit  -Close Application\n" + \
                  "\n")

        elif option.lower() == 'n':
            driver.newCustomer()
        elif option.lower() == 'a':
            driver.assignAccount()
        elif option.lower() == 'i':
            driver.accountInfo()
        elif option.lower() == 'l':
            driver.systemLog()
        elif option.lower() == 'c':
            driver.createAccount()
        elif option.lower() == 's':
            driver.suspendAccount()
        elif option.lower() == 'r':
            driver.activateAccount()
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")
            
    return None
    


def getCustomerOptions(user):
    '''
        Customer Options:
        -d  Deposit funds to account
        -w  Withdraw funds from account
        -t  Transfer funds from account1 to account2
        -l  Get customer log
    '''

    while 1:
    
        print("Enter option, for list of options enter 'help'")

        option = input()

        #print instructions for User Input
        if option.lower() == 'help':
            
            print("Valid Customer Commands:\n" + \
                  "========================\n" + \
                  "\n" + \
                  "d     -Deposit funds to account\n" + \
                  "w     -Withdraw funds from account\n" + \
                  "t     -Transfer funds from one account to another\n" + \
                  "l     -Get transaction log\n" + \
                  "exit  -Close application\n" + \
                  "\n")

        elif option.lower() == 'd':
            driver.deposit(user)
        elif option.lower() == 'w':
            driver.withdraw(user)
        elif option.lower() == 't':
            driver.transfer(user)
        elif option.lower() == 'l':
            driver.customerLog(user)
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")

    return None
    


def main():
    user = login()
    getOptions(user)
    return



main()
        
