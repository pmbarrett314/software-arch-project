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
        new_stock = Stock_Owned(owner=self, units=amount)
        new_stock.get_info(symbol)


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
                stock.delete_instance()

        else:
            raise Exception("Account cannot sell stocks it does not own")

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
          
    def __str__(self):
        return "%s: %s" % (self.symbol, self.units)

    def set_owner(self, owner):
        self.owner = owner
        self.save()

    def add_units(self, units):
        self.units += units
        self.save()

    def get_units(self):
        return self.units

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


