'''
Created Dec 3 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell


################################################
################################################
'''
import datetime

from model.stock import Stock
import model.brokerage_account 
from db.db_config import *

class Stock_Owned(DatabaseModel):
	owner = ForeignKeyField(model.brokerage_account.Brokerage_Account, related_name='owned_stocks')
	purchase_price = DoubleField(default=0.0)
	purchase_date = DateField(default=datetime.datetime.now)
	
	def get_profit_loss():
		'''
		Returns the difference between the current 
		current_price and the purchase_price
		'''
		return current_price - purchase_price

