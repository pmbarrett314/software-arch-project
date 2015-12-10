import getpass
from model.admin import Admin
from model.customer import Customer
from view.menu_data import *
import view.curse_menu
from controller.gui_driver import GUIDriver
from exceptions import *
from model.portfolio import Stock_Owned


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
            view.curse_menu.runMenu(account_menu, account_function)
            return


def select_account():
    accounts_list = list(GUIDriver.get_instance().get_brokerage_accounts())
    GUIDriver.get_instance().set_acct(
        accounts_list[view.curse_menu.display_selection_menu("Select an account", accounts_list)])
    view.curse_menu.runMenu(user_menu, user_functions)


def view_portfolio():
    portfolio_list = list(GUIDriver.get_instance().get_portfolio())
    for stock in portfolio_list:
        stock_owned = Stock_Owned.get_stock(stock)
        print(stock_owned)
    input()


def buy_stock():
    symbol = input("Enter ticker symbol: ")
    amount = int(input("Enter amount: "))
    if amount == 0:
        print("You just tried to buy 0 of a stock")
        input()
    try:
        GUIDriver.get_instance().buy(symbol, amount)
    except InsufficientFundsError as e:
        print(e)
        input()
    else:
        print("Successfully purchased %d shares of %s" % (amount, symbol))
        input()


def sell_stock():
    stocks_list = list(GUIDriver.get_instance().get_portfolio())

    selected_stock_id = stocks_list[view.curse_menu.display_selection_menu("Select a stock", stocks_list)]
    selected_stock = Stock_Owned.get_stock(selected_stock_id)
    symbol = selected_stock.symbol
    amount = int(input("Enter amount: "))

    try:
        GUIDriver.get_instance().sell(selected_stock_id, amount)
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
    pass


def search_stock():
    symbol = input("Enter ticker symbol: ")
    stock_dict = GUIDriver.get_instance().search_stock(symbol)
    print(stock_dict)
    input("Press enter when finished")


login_function = {
    "login": login,
}

account_function = {
    "select_account": select_account,

}

user_functions = {
    "view_portfolio": view_portfolio,
    "buy_stock": buy_stock,
    "sell_stock": sell_stock,
    "transaction_history": view_transaction_history,
    "search_stock": search_stock,

}


def show_view():
    view.curse_menu.runMenu(login_menu, login_function)
