import getpass
from model.admin import Admin
from model.customer import Customer
from model.portfolio import Brokerage_Account, Stock_Owned
from model.stock import Stock
from exceptions import *


class GUIDriver():
    #################################################################################
    ##  STATUS NUMBERS:           ##                                                #
    ################################                                                #
    # 0) login success                                                              #
    # 1) buy success                                                                #
    # 2) sell success                                                               #
    # 3) login fail = bad user/pass combo                                           #
    # 4) login fail = undefined error                                               #
    # 5) buy fail = insufficient funds                                              #
    # 6) buy fail = undefined error                                                 #
    # 7) sell fail = insufficient capital (user trying to sell more than they own)  #
    # 8) sell fail = undefined error                                                #
    #################################################################################


    __instance = None

    def __init__(self):
        self.user = None
        self.acct = None

    @classmethod
    def get_instance(cls):
        """
        :rtype: GUIDriver
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
    ###  Brokerage FUNCTIONS        ####
    ####################################

    def search_stock(self, ticker_symbl):
        stock = Stock()
        stock.get_info(ticker_symbl)
        stock_dict = {}
        stock_dict['symbol'] = ticker_symbl
        stock_dict['description'] = stock.description
        stock_dict['exchange'] = stock.exchange
        stock_dict['closing_price'] = stock.closing_price
        stock_dict['net_change'] = stock.net_change
        stock_dict['net_percentage'] = stock.net_percentage
        stock_dict['volume'] = stock.volume
        stock_dict['average_volume'] = stock.average_volume
        stock_dict['week_52_high'] = stock.week_52_high
        stock_dict['week_52_low'] = stock.week_52_low

        return stock_dict

    def buy(self, ticker_symbl, num_of_units):

        if not acct:
            return 6

        # Try to Buy Stock
        try:
            acct.buy_stock(ticker_symbl, num_of_units)
            return 1

        except Exception:
            return 5

    def sell(self, stock_set_id, num_of_units):

        if not acct:
            return 8
        try:
            stock = Stock_Owned.get(id=stock_set_id)
        except:
            return 8

        # Try to Sell Stock
        try:
            acct.sell_stock(num_of_units)
            return 2

        except Exception:
            return 7

        return status_number

    def get_portfolio(self):
        portfolio_dict = {}
        for each_stock in self.__get_stocks_owned():
            portfolio_dict[each_stock.id] = each_stock
        return portfolio_dict

    def get_brokerage_accounts(self):
        account_dict = {}
        for each_account in self.__get_brokerage_accounts():
            account_dict[each_account.id] = each_account
        return account_dict

    def get_transaction_history(self):
        log = []
        for each_log in self.user.get_system_log():
            log.append(str(each_log))
        return log

    ####################################
    ###  PRIVATE FUNCTIONS          ####
    ####################################
    def __get_brokerage_accounts(self):
        return self.user.brokerage_accounts

    def __get_stocks_owned(self):
        '''
        Return the stocks owned by the current account
        '''
        return self.acct.get_stocks_owned()

    def __get_profit_loss(self):
        '''
        Return the total
        '''
        # Profit/Loss:  (sell price - buy price) * #_of_units - buy commission? - sell commission?
        profit_loss = 0
        return self.acct.get_profit_loss

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

    def __get_total_profit_loss(self):
        # Profit/Loss:  (net current prices) - (net bought-at prices)
        #######
        # What's the difffernece betweeen this and __get_profit_loss?
        #######
        profit_loss = 0
        return self.acct.get_profit_loss()

    def __get_monthly_profit_loss(self):  # not sure we need to have this
        # (end of month net value) - (start of month net value)?
        # are we storing historical values?  do we go that in depth?
        pass



        # login
        # inputs:  username, password
        # return status_number - 0, 3, 4, or 5
        # search stock
        # inputs:  ticker_symbl
        # return dict of (1) symbol (2) description (3) exchange (4) closing price
        # (5) daily net change (6) daily net percentage (7) volume (8) average volume
        # (9) 52 week high (10) 52 week low
        # buy stock
        # ticker_symbl, num_of_units, username
        # return status_number - 1, 6, or 7
        # sell stock
        # inputs:  stock_set_id, num_of_units
        # return status_number - 2, 8, or 9
        # get portfolio data
        # inputs:  None
        # return dict?  maybe dict of dicts?


        # SUBFUNCTIONS/PRIVATE FUNCTIONS
        # get stocks_owned
        # get profit/loss for each stock "set"
        # get price_per_unit paid for each stock "set"
        # get current price_per_unit for each stock "set"
        # get total value of each stock "set"
        # get current profit/loss for entire portfolio
        # get monthly profit/loss?
        # get transaction history
        # inputs: None
        # return ????



        ############################
        ### My vision of the GUI: ##
        ############################

        # Start view:  login (after login you go straight to portfolio view)

        ###############################
        # Side or top bar with tabs for:
        ###############################
        # 1) Home/Portfolio (shows sell option by stock listings)
        # 2) Search/Buy (Shows buy option by stock listing)
        # 3) Transaction History
        # 4) Back button?  (to go to previous view?  maybe only for "other views")

        # Other Views:
        # Sell (when you click the "sell" button by stock you own you get this view to
        # input the number of units to sell and to confirm)

        # Buy (when you click the "buy" button by stock that you search, you get this view to
        # input the number of units to buy and to confirm)

        # Confirmation Page
        # This page displays when a buy/sell transaction is carried out successfully

        # Error:
        # This view displays when there is a transaction error based on
        # 1) insufficient funds when buying
        # 2) insufficient capital when selling


        # Total Views/Pages:  8
