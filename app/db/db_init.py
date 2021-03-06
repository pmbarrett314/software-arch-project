from db.db_config import *
from model.admin import Admin
from model.checking_account import Checking_Account
from model.customer import Customer
from model.portfolio import Brokerage_Account, Stock_Owned
from model.savings_account import Savings_Account
from model.transaction import Transaction


def createDB():
    '''
    Create the Database
    '''
    print("Creating Database")
    db.connect()
    db.create_tables(
        [Customer, Admin, Checking_Account, Savings_Account,
         Transaction, Brokerage_Account, Stock_Owned])
    print("Database Created")


def create_default_objects():
    '''
    Creates a list of default users and accounts for testing purposes
    '''
    # Create a default Admin user
    Admin(username="Admin1", password="password", first_name="Jack").save()
    print("Default Admin Created")

    cust1 = Customer(username="Customer1", password="password", first_name="John")
    cust1.save()
    print("Default Customer Created")

    Checking_Account(account_number="1", owner=cust1).save()
    print("Default Checking Account Created")

    Savings_Account(account_number="2", owner=cust1).save()
    print("Default Savings Account Created")

    cust2 = Customer(username="Customer2", password="password", first_name="Clark")
    cust2.save()
    print("Default Customer2 Created")

    Savings_Account(account_number="3", owner=cust2).save()
    print("Default Savings Account Created")

    Brokerage_Account(account_number="4", owner=cust1).save()
    print("Default Brokerage Account Created")


if __name__ == '__main__':
    try:
        createDB()
        create_default_objects()

    except:
        print("Database could not be created or already exists")
    print("Done")
