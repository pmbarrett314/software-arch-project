#from user import User
#from customer import Customer
#from account import Account
#from admin import Admin
#from checking_account import Checking_Account
#from savings_account import Savings_Account
#from transaction import Transaction
from db_config import *
from models import *
def createDB():
	'''
	Create the Database
	'''
	print("Creating Database")
	db.connect()
	db.create_tables([Customer, Admin, Account, Checking_Account, Savings_Account, Transaction])
	print("Database Created")


###############
#Testing Things
###############


#test = user.User.get(user.User.username == 'Morey')
#print(test)
#
#

def createUserAct():
	adm = Admin()
	cust = adm.create_customer("Morey", "password")
	act = Savings_Account(account_number="0123456789")
	act.save()
	adm.assign_account(act, cust)
	new_act = Checking_Account(account_number="38138383")
	new_act.save()
	adm.assign_account(new_act, cust)

def test1():
	adm = Admin()
	
	cust = Customer.get(username="Morey")
	
	
	act = Savings_Account.get(account_number="0123456789")
	new_act = Checking_Account.get(account_number="38138383")
	cust.deposit(act, 1500.0)
	cust.transfer(act, new_act, 50.0)
	cust.withdraw(new_act, 25.0)

	for each in adm.get_system_log():
		print(each)
	
	for each_account in adm.get_all_account_info():
		print(each_account)

	print(act)

if __name__ == '__main__':
	createDB()
	createUserAct()
	test1()
	print("Done")