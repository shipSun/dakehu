import database
import sqlalchemy

class Post(database.model):
	__tablename__ = 'C_CUSSERVICE_ADD_RATE_CONF'
	type     = sqlalchemy.Column('TYPE', sqlalchemy.Integer,primary_key=True)
	rate   = sqlalchemy.Column('RATE', sqlalchemy.Integer)

