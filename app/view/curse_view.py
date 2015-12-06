import getpass
from model.admin import Admin
from model.customer import Customer
from view.menuData import menuData
import view.curseMenu


def login():
    '''
    Request user credentials and logs them in as either an Admin or Customer
    '''
    user = None
    while user is None:
        username = input("Username: ")
        password = getpass.getpass()
        try:
            user = Admin.login(username, password)
        except Admin.DoesNotExist:
            try:
                user = Customer.login(username, password)
            except Customer.DoesNotExist:
                print("Invalid Login")


functions = {
    "login": login
}


def main():
    view.curseMenu.runMenu(menuData, functions)
    pass


if __name__ == "__main__":
    main()
