import user
import customer
import account
import admin
import checking_account
import savings_account
import transaction

from db_config import *
from models import *

def createDB():
	'''
	Create the Database
	'''
	print("Creating Database")
	db.connect()
	db.create_tables([customer.Customer, admin.Admin, checking_account.Checking_Account, savings_account.Savings_Account, transaction.Transaction])
	print("Database Created")


###############
#Testing Things
###############

def createUserAct():
	'''
	Creates a new Account
	'''
	adm = admin.Admin()
	cust = admin.Admin().create_customer("Customer1", "password")
	act = savings_account.Savings_Account(account_number="0123456789")
	act.save()
	adm.assign_account(act, cust)
	new_act = checking_account.Checking_Account(account_number="38138383")
	new_act.save()
	adm.assign_account(new_act, cust)

def test1():
	'''
	Some Test Transactions
	'''
	createUserAct()
	adm = admin.Admin(username = "Hey", password="password")
	adm.save()
	
	cust = customer.Customer.get(username="Customer1")
	
	
	act = savings_account.Savings_Account.get(account_number="0123456789")
	new_act = checking_account.Checking_Account.get(account_number="38138383")
	cust.deposit(act, 1500.0)
	cust.transfer(act, new_act, 50.0)
	cust.withdraw(new_act, 25.0)

	for each in adm.get_system_log():
		print(each)
	
	for each_account in adm.get_all_account_info():
		print(each_account)

	print(act)
	print(admin.Admin.login("Hey", "password"))
	print(customer.Customer.login("Customer1", "password"))
	
if __name__ == '__main__':
	#createDB()
	cust = customer.Customer.get(username="Customer1")
	act = savings_account.Savings_Account.get(account_number="0123456789")
	new_act = checking_account.Checking_Account.get(account_number="38138383")
	
	cust.deposit(act, 1500.0)
	cust.transfer(act, new_act, 50.0)
	cust.withdraw(new_act, 25.0)


	for each in admin.Admin().get_system_log():
		print(each)
	print("Done")