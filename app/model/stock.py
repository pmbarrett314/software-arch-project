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

from db.db_config import *

class Stock(DatabaseModel):
        ############################
        ###  Class Variables    ####
        ############################

        symbol = CharField()
        current_price = DoubleField(default=0.0)
        description = CharField()
        exchange = CharField()
        closing_price = DoubleField(default=0.0)
        net_change = DoubleField(default=0.0)
        net_percentage = DoubleField(default=0.0)
        volume = IntegerField(default=0)
        average_volume = IntegerField(default=0)
        week_52_high = DoubleField(default=0.0)
        week_52_low = DoubleField(default=0.0)
        
        raw_data = ""



        def get_info(self, symbol):

            self.symbol = symbol

            #get data from tradier
            #Fixed byte->String bug using the decode function as mentioned here: http://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
            self.raw_data = tradier_conn(symbol).decode()
            #print(self.raw_data)
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

        def refresh(self):
            self.get_info(self.symbol)

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
        mystock = Stock()
        mystock.get_info("GOOG")
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


