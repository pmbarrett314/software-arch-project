'''
Created Nov 19 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''



class Stock:
	############################
    ###  Class Variables
    ############################
	symbol = ""
	current_price = 0.0

	def __init__(symbol):
		self.symbol = symbol