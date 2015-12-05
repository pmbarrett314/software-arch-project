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
    # 3) login fail = user doesn't exist                                            #
    # 4) login fail = bad user/pass combo                                           #
    # 5) login fail = undefined error                                               #
    # 6) buy fail = insufficient funds                                              #
    # 7) buy fail = undefined error                                                 #
    # 8) sell fail = insufficient capital (user trying to sell more than they own)  #
    # 9) sell fail = undefined error                                                #
    #################################################################################

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
        #inputs:  customerID
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
        #inputs: customerID
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

    
