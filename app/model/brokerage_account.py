'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

from model.account import Account
from model.customer import Customer
from model.stock import Stock

from db.db_config import *


class Brokerage_Account(Account):
    ############################
    ###  Class Variables
    ############################
    owner = ForeignKeyField(Customer, related_name='brokerage_accounts', null=True)
    account_type = CharField(default="Brokerage")

    @staticmethod
    def get_account(account_number):
        '''
        Returns an account with the given account number.
        Takes a string as a parameter
        '''
        return Brokerage_Account.get(account_number=account_number)

    def get_monthly_profit_loss(self): 
        '''
        Return the monthly profit or loss for this account as a double.
        '''
        return 0.0

    def get_profit_loss(self):
        '''
        Returns the total Profit/Loss for the account
        '''
        net_profit = 0
        #Rotate through the stocks and add their
        # profit/loss to the total
        for each_stock in self.owned_stocks:
            net_profit += each_stock.get_profit_loss()
        return net_profit

    def buy_stock(self, symbol, amount):
        '''
        Buy the passed amount of stock in the company with the passed symbol
        '''
        new_stock = Stock(symbol)
        stock_price = new_stock.current_price
        
        if (stock_price * amount) > self.balance:
            raise Exception("Insufficient Funds")


    def sell_stock(self, symbol, amount):
        '''
        Sell the passed amount of stock in the company with the passed symbol
        '''
        None



