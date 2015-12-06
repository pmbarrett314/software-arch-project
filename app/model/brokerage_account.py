'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import model.account as account
import model.customer as customer

from db.db_config import *


class Brokerage_Account(account.Account):
    ############################
    ###  Class Variables
    ############################
    owner = ForeignKeyField(customer.Customer, related_name='brokerage_accounts', null=True)
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

    def buy_stock(self, symbol, amount):
        '''
        Buy the passed amount of stock in the company with the passed symbol
        '''
        None

    def sell_stock(self, symbol, amount):
        '''
        Sell the passed amount of stock in the company with the passed symbol
        '''
        None
