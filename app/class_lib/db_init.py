import user, customer, account, admin, checking_account, savings_account, log
from db_config import *

def createDB():
	'''
	Create the Database
	'''
	print("Creating Database")
	db.connect()
	db.create_tables([user.User, customer.Customer, account.Account, admin.Admin, checking_account.Checking_Account, savings_account.Savings_Account, log.Log])
	print("Database Created")


###############
#Testing Things
###############


#test = user.User.get(user.User.username == 'Morey')
#print(test)
#
#


if __name__ == '__main__':

	print("Done")