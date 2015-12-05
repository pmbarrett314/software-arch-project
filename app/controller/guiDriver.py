import getpass
from model.customer import Customer
from model.brokerage_account import Brokerage_Account
from model.stock import Stock
#from model.portfolio import Portfolio  - Whatever we're calling the "portfolio" model

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

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    ####################################
    ###  PUBLIC FUNCTIONS           ####
    ####################################

    def login(self, username, password):
        #start with bad status
        status_number = 4

        #try logging as admin
        try:
            self.user = Admin.login(username, password)
            status_number = 0
        except: Admin.DoesNotExist:
            #try logging as customer
            try:
                self.user = Customer.login(username, password)
                status_number = 0
            except Customer.DoesNotExist:
                status_number = 3
                
        return status_number
    

    def search_stock(self, ticker_symbl):
        stock = Stock(ticker_symbl)
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
        return status_number
    

    def sell(self, stock_set_id, num_of_units):
        return status_number
    

    def get_portfolio(self):
        return portfolio_dict
    

    def get_transaction_history(self):
        return something #not sure how this was handled last time




    ####################################
    ###  PRIVATE FUNCTIONS          ####
    ####################################
    def __get_stocks_owned(self):
        return stocks_array
    

    def __get_profit_loss(self):
        #Profit/Loss:  (sell price - buy price) * #_of_units - buy commission? - sell commission?
        return profit_loss
    

    def __get_buying_price(self, stock_set_id):
        return buying_price
    

    def __get_current_price(self, ticker_symbl):
        return current_price
    

    def __get_buying_value(self, stock_set_id):
        #price paid * number of shares
        return buying_value
    

    def __get_sell_value (self, stock_set_id):
        #current price * number of shares
        return sell_value
    
    
    def __get_total_profit_loss(self):
        #Profit/Loss:  (net current prices) - (net bought-at prices)
        return profit_loss
    

    def __get_monthly_profit_loss(self): #not sure we need to have this
        #(end of month net value) - (start of month net value)?
        # are we storing historical values?  do we go that in depth?
        

    
    #login
        #inputs:  username, password
        #return status_number - 0, 3, 4, or 5
    #search stock
        #inputs:  ticker_symbl
        #return dict of (1) symbol (2) description (3) exchange (4) closing price
        # (5) daily net change (6) daily net percentage (7) volume (8) average volume
        #(9) 52 week high (10) 52 week low
    #buy stock
        #ticker_symbl, num_of_units, username
        #return status_number - 1, 6, or 7
    #sell stock
        #inputs:  stock_set_id, num_of_units
        #return status_number - 2, 8, or 9
    #get portfolio data
        #inputs:  None
        #return dict?  maybe dict of dicts?

        
        #SUBFUNCTIONS/PRIVATE FUNCTIONS
            #get stocks_owned
                #get profit/loss for each stock "set"
                #get price_per_unit paid for each stock "set"
                #get current price_per_unit for each stock "set"
                #get total value of each stock "set"
            #get current profit/loss for entire portfolio
            #get monthly profit/loss?
    #get transaction history
        #inputs: None
        #return ????



    ############################
    ### My vision of the GUI: ##
    ############################

    #Start view:  login (after login you go straight to portfolio view)

        ###############################
        #Side or top bar with tabs for:
        ###############################
        #1) Home/Portfolio (shows sell option by stock listings)
        #2) Search/Buy (Shows buy option by stock listing)
        #3) Transaction History
        #4) Back button?  (to go to previous view?  maybe only for "other views")

        #Other Views:
            #Sell (when you click the "sell" button by stock you own you get this view to
            #input the number of units to sell and to confirm)

            #Buy (when you click the "buy" button by stock that you search, you get this view to
            #input the number of units to buy and to confirm)

            #Confirmation Page
            #This page displays when a buy/sell transaction is carried out successfully

            #Error:
            #This view displays when there is a transaction error based on
                #1) insufficient funds when buying
                #2) insufficient capital when selling


    #Total Views/Pages:  8

    
