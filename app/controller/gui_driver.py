from exceptions import *
from model.admin import Admin
from model.customer import Customer
from model.portfolio import Brokerage_Account, Stock_Owned
from model.stock import Stock


class GUI_Driver():
    __instance = None

    def __init__(self):
        self.user = None
        self.acct = None

    @classmethod
    def get_instance(cls):
        """
        :rtype: GUI_Driver
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def set_acct(self, id):
        self.acct = Brokerage_Account.get_account(id)

    ####################################
    ###  PUBLIC FUNCTIONS           ####
    ####################################

    def login(self, username, password):
        # try logging as admin
        try:
            self.user = Admin.login(username, password)
        except Admin.DoesNotExist:
            # try logging as customer
            try:
                self.user = Customer.login(username, password)
            except Customer.DoesNotExist:
                raise LoginError("The user and password combination you tried is invalid.")

    ####################################
    ###  BROKERAGE FUNCTIONS        ####
    ####################################

    def search_stock(self, ticker_symbl):
        stock = Stock()
        stock.get_info(ticker_symbl)
        return stock

    def buy(self, ticker_symbl, num_of_units):

        if not self.acct:
            raise NoAccountSelectedError("No account selected")

        try:
            self.acct.buy_stock(ticker_symbl, num_of_units)

        except InsufficientFundsError as e:
            raise e

    def sell(self, stock_set_id, num_of_units):

        if not self.acct:
            raise NoAccountSelectedError("No account selected")
        try:
            stock = Stock_Owned.get(id=stock_set_id)
        except Stock_Owned.DoesNotExist as e:
            raise e

        # Try to Sell Stock
        try:
            self.acct.sell_stock(stock, num_of_units)

        except StockNotOwnedError as e:
            raise e

    def get_portfolio(self):
        '''
        Returns the stocks the account owns as a dictionary
        '''
        portfolio_dict = {}
        for each_stock in self.__get_stocks_owned():
            portfolio_dict[each_stock.id] = each_stock
        return portfolio_dict

    def get_transaction_history(self):
        '''
        Returns the user's transaction history as an array
        '''
        log = []
        for each_log in self.user.get_customer_log():
            log.append(str(each_log))
        return log

    def get_brokerage_accounts(self):
        '''
        returns the brokerage accounts that the user owns as a dictionary
        '''
        brokerage_dict = {}
        for each_acct in self.__get_brokerage_accounts():
            brokerage_dict[each_acct.account_number] = each_acct
        return brokerage_dict

    def set_account(self, acct):
        '''
        Sets the given account as the Driver's acct object
        '''
        if acct in self.__get_brokerage_accounts():
            self.acct = acct
        else:
            raise AccountNotOwnedError("User does not own that account")

    def get_total_profit_loss(self):
        return self.__get_total_profit_loss()

    def get_account_balance(self):
        return self.acct.current_balance()

    ####################################
    ###  PRIVATE FUNCTIONS          ####
    ####################################

    def __get_brokerage_accounts(self):
        '''
        Return the user's Owned Brokerage brokerage_accounts
        '''
        return self.user.brokerage_accounts

    def __get_stocks_owned(self):
        '''
        Return the stocks owned by the current account
        '''
        return self.acct.get_stocks_owned()

    def __get_total_profit_loss(self):
        '''
        Return the total
        '''
        # Profit/Loss:  (sell price - buy price) * #_of_units - buy commission? - sell commission?
        profit_loss = 0
        return self.acct.get_total_profit_loss()

    def __get_buying_price(self, stock_set_id):
        '''
        Returns the price the that the stock was bought bought-at
        '''
        stk = Stock_Owned.get_stock(stock_set_id)
        return stk.purchase_price

    def __get_current_price(self, ticker_symbl):
        stk = Stock()
        stk.get_info(ticker_symbl)
        return stk.current_price

    def __get_buying_value(self, stock_set_id):
        # price paid * number of shares
        stk = Stock_Owned.get_stock(stock_set_id)
        return stk.get_buying_value()

    def __get_sell_value(self, stock_set_id):
        # current price * number of shares
        stk = Stock_Owned.get_stock(stock_set_id)
        return stk.get_value()

    def __get_profit_loss(self):
        # Profit/Loss:  (net current prices) - (net bought-at prices)
        profit_loss = 0
        return self.acct.get_current_profit_loss()

    def __get_monthly_profit_loss(self):  # not sure we need to have this
        # (end of month net value) - (start of month net value)?
        # are we storing historical values?  do we go that in depth?
        pass
