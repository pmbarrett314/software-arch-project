import getpass

from controller.gui_driver import GUI_Driver
from exceptions import *
from model.portfolio import Stock_Owned

import cursesmenu


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
            account_menu = cursesmenu.CursesMenu(title="Information", subtitle="Please select an option...")
            select_account_item = cursesmenu.items.FunctionItem("Select Account", account_menu, select_account)
            view_transaction_history_item = cursesmenu.items.FunctionItem("View Transaction History", account_menu,
                                                                          view_transaction_history)
            search_stock_item = cursesmenu.items.FunctionItem("Search Stock", account_menu, search_stock)
            account_menu.append_item(select_account_item)
            account_menu.append_item(view_transaction_history_item)
            account_menu.append_item(search_stock_item)

            account_menu.show()
            account_menu.join()
            return


def select_account():
    accounts_list = list(GUI_Driver.get_instance().get_brokerage_accounts())
    choice = view.curse_menu.display_selection_menu("Select an account", accounts_list)
    if choice == len(accounts_list):
        return
    selected_account = accounts_list[choice]
    GUI_Driver.get_instance().set_acct(selected_account)
    user_menu = cursesmenu.CursesMenu(title="Information", subtitle="Please select an option...")
    view_portfolio_item = cursesmenu.items.FunctionItem("View Portfolio", user_menu, view_portfolio)
    buy_stock_item = cursesmenu.items.FunctionItem("Buy Stock", user_menu, buy_stock)
    sell_stock_item = cursesmenu.items.FunctionItem("Sell Stock", user_menu, buy_stock)
    search_stock_item = cursesmenu.items.FunctionItem("Search Stock", user_menu, search_stock)
    user_menu.append_item(view_portfolio_item)
    user_menu.append_item(buy_stock_item)
    user_menu.append_item(sell_stock_item)
    user_menu.append_item(search_stock_item)
    user_menu.show()
    user_menu.join()


def view_portfolio():
    print("Getting portfolio information")
    total_value = 0
    portfolio_list = list(GUI_Driver.get_instance().get_portfolio().values())
    profit_loss = GUI_Driver.get_instance().get_total_profit_loss()
    acct_balance = GUI_Driver.get_instance().get_account_balance()
    for stock in portfolio_list:
        stock_value = stock.get_value()
        stock_price = stock.get_current_price(refresh=False)
        stock_repr = "%s Current: $%.2f Purchase: $%.2f %d shares Total Value: $%.2f" % \
                     (stock.symbol, stock_price, stock.purchase_price, stock.units, stock_value)
        print(stock_repr)
        total_value += stock_value
    print("Done: Total value: $%.2f; Total Profit/Loss: $%.2f; Account Balance: $%.2f" % (
        total_value, profit_loss, acct_balance))
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


def show_view():
    login_menu = cursesmenu.CursesMenu(title="Trade Net brokerage system", subtitle="Please select an option...")
    login_item = cursesmenu.items.FunctionItem("Login", login_menu, login)
    login_menu.append_item(login_item)
    login_menu.show()
    login_menu.join()
