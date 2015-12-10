import getpass
from model.checking_account import Checking_Account
from model.customer import Customer
from model.savings_account import Savings_Account
from model.admin import Admin
from model.portfolio import Brokerage_Account

# import other classes

class BankSystemDriver():
    __instance = None

    def __init__(self):
        self.user = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    #############################
    ### COMMON USER FUNCTIONS
    #############################

    def login(self):
        '''
        Request user credentials and logs them in as either an Admin or Customer
        '''
        self.user = None
        while self.user is None:
            username = input("Username: ")
            password = getpass.getpass()
            try:
                self.user = Admin.login(username, password)
            except Admin.DoesNotExist:
                try:
                    self.user = Customer.login(username, password)
                except Customer.DoesNotExist:
                    print("Invalid Login")

    def get_account(self):
        '''
        Ask the user for an account number, and return a valid account
        '''
        acct = None
        account_number = input("Account Number: ")
        # Check Savings Accounts for a match
        try:
            return Savings_Account.get_account(account_number)
        except Savings_Account.DoesNotExist:
            # Check Checking Accounts for a match
            try:
                return Checking_Account.get_account(account_number)
            except Checking_Account.DoesNotExist:
                # Check Brokerage Accounts for a match
                try:
                    return Brokerage_Account.get_account(account_number)
                except Brokerage_Account.DoesNotExist:
                    print("Account not found")
                
        return acct

    def get_amount(self):
        '''
        Ask the user for a valid amount to deposit, withdraw, or transfer
        '''
        amount = None
        try:
            amount = float(input("Enter Amount: $"))
            if amount < 0:
                amount = None
                print("Invalid Amount, amount must be positive")
        except ValueError:
            print("Invalid Amount, amount must be a positive number")
        return amount

    def get_customer(self):
        '''
        Ask the user for a username and return the customer with that username
        '''
        cust = None
        try:
            cust = Customer.get_customer(input("Username: "))
        except Customer.DoesNotExist:
            print("Could not find the customer with that username")
        return cust

    #############################
    ### ADMIN FUNCTIONS - MAIN
    #############################

    def new_customer(self):
        '''
        Creates a new customer's username and password
        '''
        username = input("Enter username: ")
        first_name = input("Enter First Name: ")
        passwd = getpass.getpass()
        try:
            self.user.create_customer(username, passwd, first_name)
            print("Customer created successfully")
        except:
            print("Error creating new customer")
        return

    def assign_account(self):
        '''
        Assign a specific account to a certain customer
        '''
        acct = self.get_account()
        if not acct:
            return
        # get customer object from username
        cust = self.get_customer()
        if not cust:
            return
        try:
            self.user.assign_account(acct, cust)
            print("Account assignment successful\n")
        except Exception as e:
            print("Error in account assignment. %s\n" % e)
        return

    def account_info(self):
        '''
        Displays all account info for all of the accounts currently stored
        '''
        print("Accounts:")
        account_array = self.user.get_all_account_info()
        for item in account_array:
            print(item)
        return

    def customer_list(self):
        '''
        Displays a list of all of the current customers stored
        '''
        customer_array = self.user.get_all_customers()
        print("Customers:")
        for item in customer_array:
            print(item)
        return

    def system_log(self):
        '''
        Displays a list of all of the transactions the system has had
        '''
        print("System Log:")
        system_log = self.user.get_system_log()
        for item in system_log:
            print(item)
        return

    def create_account(self):
        '''
        Create an account without linking it to a customer
        '''
        account_type = input("Checking, Savings account or Brokerage (c/s/b): ")
        if account_type.lower() == "c":
            acct_type = "checking"
        elif account_type.lower() == "s":
            acct_type = "savings"
        elif account_type.lower() == "b":
            acct_type = "brokerage"
        else:
            print("Invalid Account type.  Try again.")
            return
        account_number = input("Account Number: ")
        try:
            self.user.create_account(acct_type, account_number)
            print("Account %s created" % account_number)
        except Exception as e:
            print("Error creating account. %s" % e)

    def suspend_account(self):
        '''
        Suspend a certain and current customer that is stored
        '''
        try:
            # get customer object from username
            cust = self.get_customer()
            if not cust:
                return
            self.user.suspend_customer(cust)
            print("Customer suspended.\n")
        except:
            print("Problem suspending customer.  Try again.\n")

    def activate_account(self):
        '''
        Activate an account that has been suspended
        '''
        try:
            # get customer object from username
            cust = self.get_customer()
            if not cust:
                return
            self.user.activate_customer(cust)
            print("Customer activated.\n")
        except:
            print("Problem suspending account.  Try again.")

    #############################
    ### CUSTOMER FUNCTIONS - MAIN
    #############################

    def deposit(self):
        '''
        Takes the amount the customer deposited and stores it in account
        '''
        acct = self.get_account()
        if not acct:
            return
        amount = self.get_amount()
        if not amount:
            return
        try:
            self.user.deposit(acct, amount)
            print("Transaction Success: $%s deposited into %s." % (amount, acct.account_number))
        except Exception as e:
            print("Transaction Failure: %s" % (e))
        return

    def withdraw(self):
        '''
        Takes the amount the customer requests and subtracts the value from the account
        Returns value the customer requests back to them
        '''
        acct = self.get_account()
        if not acct:
            return
        amount = self.get_amount()
        if not amount:
            return
        try:
            self.user.withdraw(acct, amount)
            print("Transaction Success: $%s withdrawn from %s." % (amount, acct.account_number))
        except Exception as e:
            print("Transaction Failure: %s" % (e))
        return

    def transfer(self):
        '''
        Takes account to be withdrawn from and monetary amount from customer
        Takes account to be sent to and transfers money to that account
        Stores both sent and recieve in the log separate
        '''
        print("Which account would you like to transfer from?")
        source_acccount = self.get_account()
        if not source_acccount:
            return
        print("How much would you like to transfer?")
        amount = self.get_amount()
        if not amount:
            return
        print("Which account would you like to transfer to?")
        destination_account = self.get_account()
        if not destination_account:
            return
        try:
            self.user.transfer(source_acccount, destination_account, amount)
            print("Transaction Success: $%s trasferred from %s." % (amount, source_acccount.account_number))
        except Exception as e:
            print("Transaction Failure: %s" % (e))
        return

    def customer_log(self):
        '''
        Displays transactions made by that customer from the logs created
        '''
        for each_log in self.user.get_customer_log():
            print(each_log)
        return
