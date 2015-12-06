'''
Created Dec 4 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import datetime

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
        stk = Stock("AAPL")
        new_stock = Stock_Owned(symbol)#, self, amount)
        #stock_price = new_stock.current_price * amount)
        new_stock.set_owner(self)
        new_stock.add_units(amount)
        print(new_stock.symbol)
        if new_stock.get_value() > self.balance:
            raise Exception("Insufficient Funds")
        
        
        else:
            self.balance -= new_stock.get_value()
            new_stock.save()
            self.save()
        #print(new_stock)
        #Stock_Owned(symbol, self, amount).save()

    def sell_stock(self, symbol, amount):
        '''
        Sell the passed amount of stock in the company with the passed symbol
        '''
        None

    def get_stocks_owned(self):
        '''
        Returns the stocks that the account owned_stocks
        '''
        return self.owned_stocks




class Stock_Owned(Stock):
    owner = ForeignKeyField(Brokerage_Account, related_name='owned_stocks')
    purchase_price = DoubleField(default=0.0)
    purchase_date = DateField(default=datetime.datetime.now)
    units = IntegerField(default=0)
    '''
    def __init__(self, symbol, owner, number_of_units):
        #Based on inheritance example (line 58): https://github.com/coleifer/peewee/blob/9563dfe84c3b17a7bda0e140b750620b37d61c36/playhouse/signals.py
        super(Stock, self).__init__(symbol)
        self.purchase_price = self.current_price
        self.owner = owner
        self.units = number_of_units
    '''
    def __init__(self):
            #Call super constructor to avoid error: https://github.com/coleifer/peewee/issues/118
            super(DatabaseModel, self).__init__()
    def __str__(self):
        return "%s: %s" % (self.symbol, self.units)

    def set_owner(self, owner):
        self.owner = owner

    def add_units(self, units):
        self.units += units

    def get_value(self):
        return self.current_price * self.units

    def get_profit_loss(self):
        '''
        Returns the difference between the current 
        current_price and the purchase_price
        '''
        return (current_price - purchase_price) * units


