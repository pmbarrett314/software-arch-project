'''
Created Nov 5 2015

Project:  

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

#The Database Models


from peewee import *
from db_config import *
import datetime

class User(DatabaseModel):

    username = CharField(unique=True)
    password = CharField()
    user_type = CharField()

    def __str__(self):
        return "%s (%s)" % (self.username, self.user_type)

class Admin(User):

    ############################
    ###  Initialize class object
    ############################
    user_type = CharField(default="Admin")

    def login(username, password):
        '''
        If the Admin with the given password exists, return it
        '''
        return Admin.get(username=username, password=password)

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

    def login(username, password):
        '''
        If the Customer with the given password exists, return it
        '''
        return Customer.get(username=username, password=password)

    def deposit(self, account, amount):
        '''
        Deposit the given amount into the specified account if the user owns that account.
        '''
        #Make sure the user owns the account
        if account.owner == self:
            #Deposit the Money
            account.deposit(amount)
            Transaction.create_deposit_log(self, amount, account)

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
            Transaction.create_withdraw_log(self, amount, account)

        else:
            print("Withdraw Fail")
            #raise Exception

    def transfer(self, sourceAccount, destinationAccount, amount):
        '''
        Withdraw money from the source account and deposit 
        it in the destination account if the user owns both accounts
        '''
        #Withrdraw money from source account.
        self.withdraw(sourceAccount, amount)
        self.deposit(destinationAccount, amount)
        Transaction.create_transfer_log(self, amount, destinationAccount, sourceAccount)

    def get_customer_log(self):
        '''
        Returns the transaction log relating to the Customer
        '''
        return self.transactions

class Account(DatabaseModel):

    ############################
    ###  Initialize class object
    ############################
    account_number = CharField(unique=True)
    balance = DoubleField(default=0.0)
    account_type = CharField()
    owner = ForeignKeyField(Customer, related_name="accounts", null=True)

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
            pass
            #throw Exception

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

    def __str__(self):
        return "%s: (%s) %s" % (self.time, self.owner, self.details)
        
    def create_withdraw_log(customer, amount, account):
        '''
        Returns the log for a withdrawl by the given user for the amount and from
        the specified account
        '''
        content = "%s: $%s withdrawn. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    def create_deposit_log(customer, amount, account):
        '''
        Returns the log for a deposited by the given user for the amount and into
        the specified account
        '''
        content = "%s: $%s deposited. New Balance: $%s" % (account.account_number, amount, account.current_balance())
        Transaction(value=amount, owner=customer, details=content).save()

    def create_transfer_log(customer, amount, to_account, from_account):
        '''
        Returns the log for a transfer by the given user for the amount and from
        from_account and into to_account
        '''
        content = "%s: $%s trasfered to %s. New Balance: $%s (%s); $%s (%s)" % (from_account.account_number, amount, to_account.account_number, 
                                                                from_account.current_balance(), from_account.account_number, 
                                                                to_account.current_balance(), to_account.account_number)
        Transaction(value=amount, owner=customer, details=content).save()









