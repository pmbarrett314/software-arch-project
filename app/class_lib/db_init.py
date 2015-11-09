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

	
if __name__ == '__main__':
	try:
		createDB()
	except:
		print("Database could not be created or already exists")
	print("Done")