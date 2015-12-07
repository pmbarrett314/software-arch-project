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
from model.stock import *
from model.transaction import Transaction
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
        new_stock = Stock_Owned()
        new_stock.setup(symbol, self, amount)


        if new_stock.get_value() > self.balance:
            raise Exception("Insufficient Funds")
        
        else:
            self.balance -= new_stock.get_value()
            new_stock.save()
            self.save()
            Transaction.buy_stock(self.owner, amount, self, new_stock)


    def sell_stock(self, stock, amount):
        '''
        Sell the passed amount of stock in the company with the passed symbol
        '''
        if stock.owner == self:
            self.balance += stock.sell_units(amount)
            self.save()
            Transaction.sell_stock(self.owner, amount, self, stock)
            if stock.units == 0:
                stock.delete()
        else:
            raise Exception("Account cannot sell stocks it does not own")

    def get_stocks_owned(self):
        '''
        Returns the stocks that the account owned_stocks
        '''
        return self.owned_stocks




class Stock_Owned(DatabaseModel):
    owner = ForeignKeyField(Brokerage_Account, related_name='owned_stocks')
    purchase_price = DoubleField(default=0.0)
    purchase_date = DateField(default=datetime.datetime.now)
    units = IntegerField(default=0)
    symbol = CharField()
    current_price = DoubleField(default=0.0)
    description = CharField()
    exchange = CharField()
    closing_price = DoubleField(default=0.0)
    net_change = DoubleField(default=0.0)
    net_percentage = DoubleField(default=0.0)
    volume = IntegerField(default=0)
    average_volume = IntegerField(default=0)
    week_52_high = DoubleField(default=0.0)
    week_52_low = DoubleField(default=0.0)
    
    raw_data = ""


    def __init__(self):
            #Call super constructor to avoid error: https://github.com/coleifer/peewee/issues/118
            super(DatabaseModel, self).__init__()
    
    def setup(self, symbol, owner, amount):
        #Call super constructor to avoid error: https://github.com/coleifer/peewee/issues/118
        super(DatabaseModel, self).__init__()
        self.owner = owner
        self.units = amount
        self.symbol = symbol

        #get data from tradier
        #Fixed byte->String bug using the decode function as mentioned here: http://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
        self.raw_data = tradier_conn(symbol).decode()
        tradier_dict = json.loads(self.raw_data)

        #parse tradier data
        self.current_price = get_price(tradier_dict)
        self.description = get_ticker_description(tradier_dict) #should be a description of the company name
        self.exchange = get_exchange(tradier_dict)
        self.closing_price = get_closing_price(tradier_dict)
        self.net_change = get_net_change(tradier_dict)
        self.net_percentage = get_net_percentage(tradier_dict)
        self.volume = get_volume(tradier_dict)
        self.average_volume = get_average_volume(tradier_dict)
        self.week_52_high = get_52_week_high(tradier_dict)
        self.week_52_low = get_52_week_low(tradier_dict)
        
        return
        
    def __str__(self):
        return "%s: %s" % (self.symbol, self.units)

    def set_owner(self, owner):
        self.owner = owner
        self.save()

    def add_units(self, units):
        self.units += units
        self.save()

    def sell_units(self, amount):
        '''
        Removes the given number of units and returns their value
        '''
        if amount > self.units:
            raise Exception("Can Only Sell %s Units of this stock" % self.units)
        self.units -= amount
        self.save()
        return self.current_price * amount

    def get_value(self):
        return self.current_price * self.units

    def get_profit_loss(self):
        '''
        Returns the difference between the current 
        current_price and the purchase_price
        '''
        return (current_price - purchase_price) * units


