from user import User
from customer import Customer
from account import Account
from admin import Admin
from checking_account import Checking_Account
from savings_account import Savings_Account
from log import Log
from db_config import *

def createDB():
	'''
	Create the Database
	'''
	print("Creating Database")
	db.connect()
	db.create_tables([Customer, Admin, Checking_Account, Savings_Account, Log])
	print("Database Created")


###############
#Testing Things
###############


#test = user.User.get(user.User.username == 'Morey')
#print(test)
#
#

if __name__ == '__main__':
	#createDB()

	#adm = Admin()
	#check = Checking_Account(account_number="0123456789")

	#cust = adm.create_customer("Morey", "password")
	cust = Customer.get(username="Morey")
	#adm.assign_account(check, cust)
	print(cust)
	print("Done")