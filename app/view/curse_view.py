import getpass
from model.admin import Admin
from model.customer import Customer
from view.menuData import *
import view.curseMenu
from controller.guiDriver import GUIDriver
from exceptions import *


def login():
    '''
    Request user credentials and logs them in as either an Admin or Customer
    '''

    user = None
    while user is None:
        username = input("Username: ")
        password = getpass.getpass()
        try:
            GUIDriver.get_instance().login(username, password)
        except LoginError as e:
            print(str(e))
            input()
            return
        else:
            view.curseMenu.runMenu(user_menu, functions)
            return


functions = {
    "login": login
}


def show_view():
    view.curseMenu.runMenu(login_menu, functions)
