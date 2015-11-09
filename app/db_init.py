import class_lib.user as user
import class_lib.customer as customer
import class_lib.account as account
import class_lib.admin as admin
import class_lib.checking_account as checking_account
import class_lib.savings_account as savings_account
import class_lib.transaction as transaction

from class_lib.db_config import *

def createDB():
	'''
	Create the Database
	'''
	print("Creating Database")
	db.connect()
	db.create_tables([customer.Customer, admin.Admin, checking_account.Checking_Account, savings_account.Savings_Account, transaction.Transaction])
	print("Database Created")

	
if __name__ == '__main__':
	try:
		createDB()
		#Create a default Admin user
		admin.Admin(username="Admin1", password="password").save()
		print("Default Admin Created")
		cust = customer.Customer(username="Customer1", password="password")
		cust.save()
		print("Default Customer Created")
		checking_account.Checking_Account(account_number="1", owner=cust).save()
		print("Default Checking Account Created")
		savings_account.Savings_Account(account_number="2", owner=cust).save()
		print("Default Savings Account Created")
	except:
		print("Database could not be created or already exists")
	print("Done")