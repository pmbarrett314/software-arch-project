import os

from peewee import *

dbpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "bank.db")

db = SqliteDatabase(dbpath)


class DatabaseModel(Model):
    class Meta:
        database = db
