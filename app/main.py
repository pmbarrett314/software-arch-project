import os
import sys
import warnings
import traceback
from class_lib.driver import BankSystemDriver as driver
import class_lib.admin as admin
import class_lib.customer as customer


def get_options(user):
    if isinstance(user, admin.Admin):
        get_admin_options()
    elif isinstance(user, customer.Customer):
        get_customer_options()
    else:
        print("Login error: Account type invalid")
        return


def get_admin_options():

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
            driver.get_instance().newCustomer()
        elif option.lower() == 'a':
            driver.get_instance().assignAccount()
        elif option.lower() == 'i':
            driver.get_instance().accountInfo()
        elif option.lower() == 'l':
            driver.get_instance().systemLog()
        elif option.lower() == 'c':
            driver.get_instance().createAccount()
        elif option.lower() == 's':
            driver.get_instance().suspendAccount()
        elif option.lower() == 'r':
            driver.get_instance().activateAccount()
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")


def get_customer_options():
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
            driver.get_instance().deposit()
        elif option.lower() == 'w':
            driver.get_instance().withdraw()
        elif option.lower() == 't':
            driver.get_instance().transfer()
        elif option.lower() == 'l':
            driver.get_instance().customerLog()
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")


def main():
    driver.get_instance().login()
    get_options(driver.get_instance().user)
    return

if __name__ == "__main__":
    main()
