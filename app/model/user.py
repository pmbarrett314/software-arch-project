'''
Created Nov 5 2015

Project:

@authors:  Paul Barrett, Morey Wood, Kristen Massey, Daniel Waddell

################################################
################################################
'''

from db.db_config import *


class User(DatabaseModel):
    ############################
    ###  Class Variables
    ############################
    username = CharField(unique=True)
    password = CharField()
    user_type = CharField()

    def __str__(self):
        return "%s (%s)" % (self.username, self.user_type)

    @staticmethod
    def login(username, password):
        '''
        If the Customer with the given password exists, return it
        Takes two strings as parameters
        '''
        return User.get(username=username, password=password)
