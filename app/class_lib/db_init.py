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
	except:
		print("Database could not be created or already exists")
	print("Done")