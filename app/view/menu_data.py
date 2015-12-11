'''
Created on Oct 7, 2014

@author: Paul
'''

from view.curse_menu import menuItem

initial_menu = {
    'title': "Trade Net", 'type': menuItem.MENU, 'subtitle': "Which System would you like to use?",
    'options': [
        {'title': "Old System", 'type': menuItem.FUNCTION, 'function': "old_system"},
        {'title': "New System", 'type': menuItem.FUNCTION, 'function': "new_system"},
    ]
}

login_menu = {
    'title': "Trade Net brokerage system", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
    'options': [
        {'title': "Login", 'type': menuItem.FUNCTION, 'function': "login"},
    ]
}

account_menu = {
    'title': "Trade Net brokerage system", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
    'options': [
        {'title': "Select Account", 'type': menuItem.FUNCTION, 'function': "select_account"},
        {'title': "View Transaction History", 'type': menuItem.FUNCTION, 'function': 'transaction_history'},
        {'title': "Search Stock", 'type': menuItem.FUNCTION, 'function': 'search_stock'},
    ]
}

user_menu = {'title': "Information", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
             'options': [
                 {'title': "View Portfolio", 'type': menuItem.FUNCTION, 'function': "view_portfolio"},
                 {'title': "Buy Stock", 'type': menuItem.FUNCTION, 'function': "buy_stock"},
                 {'title': "Sell Stock", 'type': menuItem.FUNCTION, 'function': 'sell_stock'},
                 {'title': "Search Stock", 'type': menuItem.FUNCTION, 'function': 'search_stock'},
             ]
             }
