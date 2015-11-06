from peewee import *
from db_config import *
import datetime

class User(DatabaseModel):

    username = CharField(unique=True)
    password = CharField()
    user_type = CharField()

class Admin(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Admin")
    #def __init__(self):
    #    return None

    def create_customer(self, username, password):
        '''
        Creates a new customer object
        '''
        customer = Customer(username=username, password=password)
        customer.save()
        return customer

    def assign_account(self, account, customer):
        '''
        Assign an account to a customer
        '''
        account.owner = customer
        account.save()

    def get_all_account_info(self):
        '''
        Retrieves infomration about all of the accounts as an array of strings
        '''
        accounts = []
        for each_account in Savings_Account.select():
            accounts.append(str(each_account))
        for each_account in Checking_Account.select():
            accounts.append(str(each_account))
        return accounts

    def get_system_log(self):
        '''
        Retrieves all of the transactions from the system
        '''
        return Transaction.select()

    #def create_bank_account(self):
    #    return account

    def suspend_customer(self, customer):
        '''
        Make the Customer Inactive
        '''
        customer.active = False
        customer.save()

    def activate_customer(self, customer):
        '''
        Make the Cusomter Active
        '''
        customer.active = True
        customer.save()

class Customer(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Customer")
    active = BooleanField(default=True)

    def __str__(self):
        return self.username

    def deposit(self, account, amount):
        #Make sure the user owns the account
        if account.owner == self:
            #Deposit the Money
            account.deposit(amount)
            transactionDetails = "Deposited %s into %s leaving %s in the account." % (amount, account.account_number, account.current_balance())
            new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
            new_transaction.save()
        else:
            print("Deposit Fail")
            #raise Exception


    def withdraw(self, account, amount):
        '''
        Withdraw money from the given account
        '''
        #Make sure the user owns the account
        if account.owner == self:
            account.withdraw(amount)
            transactionDetails = "Withdrew %s from %s leaving %s in the account." % (amount, account.account_number, account.current_balance())
            new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
            new_transaction.save()
        else:
            print("Withdraw Fail")
            #raise Exception

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit 
        it in the destination account
        '''
        #Withrdraw money from source account.
        self.withdraw(sourceAccount, amount)
        self.deposit(destinationAccount, amount)
        transactionDetails = "Transferred %s from %s to %s. New Balances: %s (%s); %s (%s)" % (amount, sourceAccount.account_number, destinationAccount.account_number, sourceAccount.account_number, sourceAccount.current_balance(), destinationAccount.account_number, destinationAccount.current_balance())
        new_transaction = Transaction(value=amount, owner=self, details=transactionDetails)
        new_transaction.save()
    def get_customer_log(self):
        return self.transactions

class Account(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    account_number = CharField(unique=True)
    balance = DoubleField(default=0.0)
    account_type = CharField()

    owner = ForeignKeyField(Customer, related_name="accounts", null=True)


    #def __init__(self, account_number = 0, balance = 0.00, type = ''):
    #    return None

    def __str__(self):
        return "Account Number: %s; Owner: %s; (%s Account): $%s" % (self.account_number, self.owner, self.account_type, self.balance)

    def current_balance(self):
        '''
        Get the current balance of the account
        '''
        return self.balance
    
    def deposit(self, depositAmount):
        '''
        Deposit money into the account
        '''
        self.balance += depositAmount
        self.save()

    def withdraw(self, withdrawAmount):
        '''
        Withdraw money from the account
        '''
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount
            self.save()

        else:
            pass#throw Exception

class Savings_Account(Account):
    owner = ForeignKeyField(Customer, related_name='savings_accounts', null=True)
    account_type = CharField(default="Savings")

class Checking_Account(Account):
    owner = ForeignKeyField(Customer, related_name='checking_accounts', null=True)
    account_type = CharField(default="Checking")

class Transaction(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################

    time = DateField(default=datetime.datetime.now)
    owner = ForeignKeyField(Customer, related_name='transactions')
    details = CharField()
    
    #def __init__(self, log_content="", start=None, end=None):
    #    return None

    def __str__(self):
        return "%s: (%s) %s" % (self.time, self.owner, self.details)
        














