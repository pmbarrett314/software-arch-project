import getpass
from model.admin import Admin
from model.customer import Customer
from view.menu_data import *
import view.curse_menu
from controller.gui_driver import GUIDriver
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
            view.curse_menu.runMenu(user_menu, user_functions)
            return


def view_portfolio():
    pass


def buy_stock():
    symbol = input("Enter ticker symbol")
    amount = input("Enter amount")


def sell_stock():
    symbol = input("Enter ticker symbol")
    amount = input("Enter amount")

def view_transaction_history():
    pass


login_function = {
    "login": login,

}

user_functions = {
    "view_portfolio": view_portfolio,
    "buy_stock": buy_stock,
    "sell_stock": sell_stock,
    "transaction_history": view_transaction_history

}



def show_view():
    view.curse_menu.runMenu(login_menu, login_function)
