'''
Created Nov 19 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

import urllib2
import xml.etree.ElementTree as elementTree


class Stock:
        ############################
        ###  Class Variables
        ############################
        symbol = ""
        current_price = 0.0
        description = ""

        def __init__(self, symbol):
                self.symbol = symbol
                print symbol + "\n"
                tradier_xml = tradier_conn(symbol)
                self.current_price = get_price(tradier_xml)
                self.description = get_ticker_description(tradier_xml) #should be a description of the company name?
                return

def tradier_conn(symbol):
        conn = urllib2.Request('https://api.tradier.com/v1/markets/quotes?symbols=%s' % symbol)
        conn.add_header('Authorization', 'Bearer AS3tVA7ZLKmG25NuY4aL7HhyRLME') #NOTE:  THE BEARER CODE MUST BE REACTIVATED EVERY 24 HOURS
        result = urllib2.urlopen(conn)
        return result
                

def get_price(xml_file):
        root = elementTree.fromstring(xml_file)
        element = root.findall('ask')
        current_ask = element.attrib
        print "Ask: " + current_ask + "\n"
        return current_ask

def get_ticker_description(xml_file):
        root = elementTree.fromstring(xml_file)
        element = root.findall('description')
        description = element.attrib
        print "Description: " + description + "\n"
        return description

def main():
        mystock = Stock("GOOG")

                                                                
if __name__ == '__main__':
        main()


        #Steps:
        #       1) connect to tradier with access token
        #       2) create query for market data on ticker symbol self.symbol
        #       3) get xml file with data on self.symbol
        #       4) parse xml for stock price
        #       5) parse xml for company name
                
                
