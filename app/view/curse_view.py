import getpass

import view.curse_menu
from controller.gui_driver import GUIDriver
from exceptions import *
from model.portfolio import Stock_Owned
from view.menu_data import *


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
            view.curse_menu.runMenu(account_menu, user_functions)
            return


def select_account():
    accounts_list = list(GUIDriver.get_instance().get_brokerage_accounts())
    selected_account = accounts_list[view.curse_menu.display_selection_menu("Select an account", accounts_list)]
    GUIDriver.get_instance().set_acct(selected_account)
    view.curse_menu.runMenu(user_menu, account_functions)


def view_portfolio():
    portfolio_list = list(GUIDriver.get_instance().get_portfolio().values())
    for stock in portfolio_list:
        stock_repr="%s $%.2f %d shares Total Value: $%.2f" % (stock.symbol, stock.get_current_price(), stock.units, stock.get_value())
        print(stock_repr)
    input()


def buy_stock():
    symbol = input("Enter ticker symbol: ")
    amount = int(input("Enter amount: "))
    if amount == 0:
        print("You just tried to buy 0 of a stock")
        input()
        return
    try:
        GUIDriver.get_instance().buy(symbol, amount)
    except InsufficientFundsError as e:
        print(e)
        input()
    else:
        print("Successfully purchased %d shares of %s" % (amount, symbol))
        input()


def sell_stock():
    stocks_list = list(GUIDriver.get_instance().get_portfolio().values())
    choice=view.curse_menu.display_selection_menu("Select a stock", stocks_list)
    if choice == len(stocks_list):
        return
    selected_stock = stocks_list[choice]
    symbol = selected_stock.symbol
    amount = int(input("Enter amount: "))

    if amount == 0:
        print("You just tried to buy 0 of a stock")
        input()
        return

    try:
        GUIDriver.get_instance().sell(selected_stock.id, amount)
    except StockNotOwnedError as e:
        print(e)
        input()
    except Stock_Owned.DoesNotExist as e:
        print("A database error occured in your sale")
        input()
    except NotEnoughStockOwnedError as e:
        print(e)
        input()
    else:
        print("Successfully sold %d shares of %s" % (amount, symbol))
        input()


def view_transaction_history():
    for i in GUIDriver.get_instance().get_transaction_history():
        print(i)
    input()


def search_stock():
    symbol = input("Enter ticker symbol: ")
    stock_dict = GUIDriver.get_instance().search_stock(symbol)
    print(stock_dict)
    input("Press enter when finished")


login_function = {
    "login": login,
}

user_functions = {
    "select_account": select_account,
    "transaction_history": view_transaction_history,

}

account_functions = {
    "view_portfolio": view_portfolio,
    "buy_stock": buy_stock,
    "sell_stock": sell_stock,
    "search_stock": search_stock,

}


def show_view():
    view.curse_menu.runMenu(login_menu, login_function)
