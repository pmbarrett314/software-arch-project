import os
import sys
import warnings
import traceback
from class_lib.driver import BankSystemDriver as driver
import class_lib.admin as admin
import class_lib.customer as customer


def get_options(user):
    if isinstance(user, admin.Admin):
        get_admin_options(user)
    elif isinstance(user, customer.Customer):
        get_customer_options(user)
    else:
        print("Login error: Account type invalid")
        return


def get_admin_options(user):

    while 1:

        print("Enter option, for list of options enter 'help'")

        option = input()

        # print instructions for User Input
        if option.lower() == 'help':

            print("Valid Admin Commands:\n" +
                  "=====================\n" +
                  "\n" +
                  "n     -New Customer\n" +
                  "a     -Assign Account\n" +
                  "i     -Info on Accounts\n" +
                  "l     -Get System Log\n" +
                  "c     -Create Account\n" +
                  "s     -Suspend Account\n" +
                  "r     -Reactivate/Activate Account\n" +
                  "exit  -Close Application\n" +
                  "\n")

        elif option.lower() == 'n':
            driver.newCustomer(user)
        elif option.lower() == 'a':
            driver.assignAccount(user)
        elif option.lower() == 'i':
            driver.accountInfo(user)
        elif option.lower() == 'l':
            driver.systemLog(user)
        elif option.lower() == 'c':
            driver.createAccount(user)
        elif option.lower() == 's':
            driver.suspendAccount(user)
        elif option.lower() == 'r':
            driver.activateAccount(user)
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")

    return None



def get_customer_options(user):
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

        # print instructions for User Input
        if option.lower() == 'help':

            print("Valid Customer Commands:\n" +
                  "========================\n" +
                  "\n" +
                  "d     -Deposit funds to account\n" +
                  "w     -Withdraw funds from account\n" +
                  "t     -Transfer funds from one account to another\n" +
                  "l     -Get transaction log\n" +
                  "exit  -Close application\n" +
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
    user = driver.login()
    get_options(user)
    return

if __name__ == "__main__":
    main()
