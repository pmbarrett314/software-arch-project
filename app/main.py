import model.customer as customer
from controller.driver import BankSystemDriver as Driver

from model import admin as admin


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
                  "u     -Customer List\n" +
                  "l     -Get System Log\n" +
                  "c     -Create Account\n" +
                  "s     -Suspend Account\n" +
                  "r     -Reactivate/Activate Account\n" +
                  "exit  -Close Application\n" +
                  "\n")

        # Call the appropriate function for the given menu option
        elif option.lower() == 'n':
            Driver.get_instance().new_customer()
        elif option.lower() == 'a':
            Driver.get_instance().assign_account()
        elif option.lower() == 'i':
            Driver.get_instance().account_info()
        elif option.lower() == 'u':
            Driver.get_instance().customer_list()
        elif option.lower() == 'l':
            Driver.get_instance().system_log()
        elif option.lower() == 'c':
            Driver.get_instance().create_account()
        elif option.lower() == 's':
            Driver.get_instance().suspend_account()
        elif option.lower() == 'r':
            Driver.get_instance().activate_account()

        # Exit
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

        # Call the appropriate function for the given menu option
        elif option.lower() == 'd':
            Driver.get_instance().deposit()
        elif option.lower() == 'w':
            Driver.get_instance().withdraw()
        elif option.lower() == 't':
            Driver.get_instance().transfer()
        elif option.lower() == 'l':
            Driver.get_instance().customer_log()

        # Exit
        elif option.lower() == 'exit':
            break
        else:
            print("Invalid input.\n")


def main():
    Driver.get_instance().login()
    get_options(Driver.get_instance().user)
    return


if __name__ == "__main__":
    main()
