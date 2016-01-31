import view.curse_view
from controller.driver import BankSystemDriver as Driver
from model.admin import Admin
from model.customer import Customer

import cursesmenu


def get_options(user):
    if isinstance(user, Admin):
        get_admin_options()
    elif isinstance(user, Customer):
        get_customer_options()
    else:
        print("Login error: Account type invalid")


def get_admin_options():
    while 1:

        print("Enter option, for list of options enter 'help'")

        option = input().lower()

        # print instructions for User Input
        if option == 'help':

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
        elif option == 'n':
            Driver.get_instance().new_customer()
        elif option == 'a':
            Driver.get_instance().assign_account()
        elif option == 'i':
            Driver.get_instance().account_info()
        elif option == 'u':
            Driver.get_instance().customer_list()
        elif option == 'l':
            Driver.get_instance().system_log()
        elif option == 'c':
            Driver.get_instance().create_account()
        elif option == 's':
            Driver.get_instance().suspend_account()
        elif option == 'r':
            Driver.get_instance().activate_account()

        # Exit
        elif option == 'exit':
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

        option = input().lower()

        # print instructions for User Input
        if option == 'help':

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
        elif option == 'd':
            Driver.get_instance().deposit()
        elif option == 'w':
            Driver.get_instance().withdraw()
        elif option == 't':
            Driver.get_instance().transfer()
        elif option == 'l':
            Driver.get_instance().customer_log()

        # Exit
        elif option == 'exit':
            break
        else:
            print("Invalid input.\n")


def old_system():
    Driver.get_instance().login()
    get_options(Driver.get_instance().user)


def new_system():
    view.curse_view.show_view()


def main():
    initial_menu = cursesmenu.CursesMenu(title="Trade Net", subtitle="Which System would you like to use?")
    old_item = cursesmenu.items.FunctionItem("Old System", initial_menu, old_system)
    new_item = cursesmenu.items.FunctionItem("New System", initial_menu, new_system)
    initial_menu.append_item(old_item)
    initial_menu.append_item(new_item)
    initial_menu.show()
    initial_menu.join()


if __name__ == "__main__":
    main()
