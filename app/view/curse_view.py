import getpass

import view.curse_menu
from controller.gui_driver import GUI_Driver
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
            GUI_Driver.get_instance().login(username, password)
        except LoginError as e:
            print(str(e))
            input()
            return
        else:
            view.curse_menu.runMenu(account_menu, user_functions)
            return


def select_account():
    accounts_list = list(GUI_Driver.get_instance().get_brokerage_accounts())
    choice = view.curse_menu.display_selection_menu("Select an account", accounts_list)
    if choice == len(accounts_list):
        return
    selected_account = accounts_list[choice]
    GUI_Driver.get_instance().set_acct(selected_account)
    view.curse_menu.runMenu(user_menu, account_functions)


def view_portfolio():
    print("Getting portfolio information")
    total_value = 0
    portfolio_list = list(GUI_Driver.get_instance().get_portfolio().values())
    profit_loss = GUI_Driver.get_instance().get_total_profit_loss()
    for stock in portfolio_list:
        stock_value = stock.get_value()
        stock_price = stock.get_current_price(refresh=False)
        stock_repr = "%s Current: $%.2f Purchase: $%.2f %d shares Total Value: $%.2f" % \
                     (stock.symbol, stock_price, stock.purchase_price, stock.units, stock_value)
        print(stock_repr)
        total_value += stock_value
    print("Done: Total value: $%.2f; Total Profit/Loss: $%.2f" % (total_value, profit_loss))
    input()


def buy_stock():
    symbol = input("Enter ticker symbol: ")
    amount = int(input("Enter amount: "))
    if amount == 0:
        print("You just tried to buy 0 of a stock")
        input()
        return
    try:
        GUI_Driver.get_instance().buy(symbol, amount)
    except InsufficientFundsError as e:
        print(e)
        input()
    else:
        print("Successfully purchased %d shares of %s" % (amount, symbol))
        input()


def sell_stock():
    stocks_list = list(GUI_Driver.get_instance().get_portfolio().values())
    choice = view.curse_menu.display_selection_menu("Select a stock", stocks_list)
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
        GUI_Driver.get_instance().sell(selected_stock.id, amount)
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
    for i in GUI_Driver.get_instance().get_transaction_history():
        print(i)
    input()


def search_stock():
    symbol = input("Enter ticker symbol: ")
    stock = GUI_Driver.get_instance().search_stock(symbol)
    print(stock.description)
    print("Exchange: %s" % stock.exchange)
    print("Price: %f" % stock.current_price)
    print("Net Change: $%.2f Percent: %%%.2f" % (stock.net_change, stock.net_percentage))
    print("Volume: %d Average: %d" % (stock.volume, stock.average_volume))
    print("52 Week Low: $%.2f High: $%.2f" % (stock.week_52_low, stock.week_52_high))
    input("Press enter when finished")


login_function = {
    "login": login,
}

user_functions = {
    "select_account": select_account,
    "transaction_history": view_transaction_history,
    "search_stock": search_stock,

}

account_functions = {
    "view_portfolio": view_portfolio,
    "buy_stock": buy_stock,
    "sell_stock": sell_stock,
    "search_stock": search_stock,

}


def show_view():
    view.curse_menu.runMenu(login_menu, login_function)
