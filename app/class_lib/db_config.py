from peewee import *

db = SqliteDatabase('bank.db')

class DatabaseModel(Model):
	class Meta:
		database = db