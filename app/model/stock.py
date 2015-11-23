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
        ###  Class Variables
        ############################
        symbol = ""
        current_price = 0.0
        description = ""
        raw_data = ""

        def __init__(self, symbol):
                self.symbol = symbol

                #get data from tradier
                self.raw_data = tradier_conn(symbol)
                tradier_dict = json.loads(self.raw_data)

                #parse tradier data
                self.current_price = get_price(tradier_dict)
                self.description = get_ticker_description(tradier_dict) #should be a description of the company name?
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


