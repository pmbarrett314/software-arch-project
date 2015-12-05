'''
Created Nov 19 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

Sources:        https://developer.tradier.com/documentation/markets/get-quotes
                https://developer.tradier.com/documentation/examples/python
                https://developer.tradier.com/getting_started

################################################
################################################
'''

import http.client
import json


class Stock:
        ############################
        ###  Class Variables    ####
        ############################
        symbol = ""
        current_price = 0.00
        description = ""
        exchange = ""
        closing_price = 0.00
        net_change = 0.00
        net_percentage = 0.00
        volume = 0
        average_volume = 0
        week_52_high = 0.00
        week_52_low = 0.00
        
        raw_data = ""

        def __init__(self, symbol):
                self.symbol = symbol

                #get data from tradier
                self.raw_data = tradier_conn(symbol)
                tradier_dict = json.loads(self.raw_data)

                #parse tradier data
                self.current_price = get_price(tradier_dict)
                self.description = get_ticker_description(tradier_dict) #should be a description of the company name
                self.exchange = get_exchange(tradier_dict)
                self.closing_price = get_closing_price(tradier_dict)
                self.net_change = get_net_change(tradier_dict)
                self.net_percentage = get_net_percentage(tradier_dict)
                self.volume = get_volume(tradier_dict)
                self.average_volume = get_average_volume(tradier_dict)
                self.week_52_high = get_52_week_high(tradier_dict)
                self.week_52_low = get_52_week_low(tradier_dict)
                
                return

def tradier_conn(symbol):

        ###############################
        ###  START OF TRADIER CODE  ###
        ###############################
        # Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)

        connection = http.client.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)

        # Headers

        headers = {"Accept":"application/json",
                   "Authorization":"Bearer UAiiqlYjW80rzD0u5wC6FMAQMF4v"}

        # Send synchronously

        connection.request('GET', '/v1/markets/quotes?symbols=%s' % symbol, None, headers)
        try:
                response = connection.getresponse()
                content = response.read()
                # Success
                #print('Response status ' + str(response.status))
        except http.client.HTTPException as e:
                # Exception
                print('Exception during request')

        #############################
        ###  END OF TRADIER CODE  ###
        #############################
        return content


def get_price(tradier_dict):
        current_ask = tradier_dict["quotes"]["quote"]["ask"]
        return current_ask

def get_ticker_description(tradier_dict):
        description = tradier_dict["quotes"]["quote"]["description"]
        return description

def get_exchange(tradier_dict):
        exchange = tradier_dict["quotes"]["quote"]["exch"]
        return exchange

def get_closing_price(tradier_dict):
        closing_price = tradier_dict["quotes"]["quote"]["prevclose"]
        return closing_price

def get_net_change(tradier_dict):
        net_change = tradier_dict["quotes"]["quote"]["change"]
        return net_change

def get_net_percentage(tradier_dict):
        net_percentage = tradier_dict["quotes"]["quote"]["change_percentage"]
        return net_percentage

def get_volume(tradier_dict):
        volume = tradier_dict["quotes"]["quote"]["volume"]
        return volume

def get_average_volume(tradier_dict):
        average_volume = tradier_dict["quotes"]["quote"]["average_volume"]
        return average_volume

def get_52_week_high(tradier_dict):
        week_52_high = tradier_dict["quotes"]["quote"]["week_52_high"]
        return week_52_high

def get_52_week_low(tradier_dict):
        week_52_low = tradier_dict["quotes"]["quote"]["week_52_low"]
        return week_52_low

def main():
        mystock = Stock("GOOG")
        print("Stock is: " + str(mystock.description) + "\n")
        print("Stock price: " + str(mystock.current_price) + "\n")
        print("raw data: \n")
        print(mystock.raw_data)


if __name__ == '__main__':
        main()


        #Steps:
        #       1) connect to tradier with access token
        #       2) create query for market data on ticker symbol self.symbol
        #       3) get xml file with data on self.symbol
        #       4) parse xml for stock price
        #       5) parse xml for company name


