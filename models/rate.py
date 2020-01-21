import database
import sqlalchemy
import datetime

class Conf(database.model,database.Action):
    __tablename__ = 'C_CUSSERVICE_ADD_RATE_CONF'
    type = sqlalchemy.Column('TYPE', sqlalchemy.Integer, primary_key=True)
    rate = sqlalchemy.Column('RATE', sqlalchemy.Integer)
    multiply = sqlalchemy.Column('MULTIPLY',sqlalchemy.Integer)
    creation_date = sqlalchemy.Column('CREATIONDATE', sqlalchemy.Date)
    modified_date = sqlalchemy.Column('MODIFIEDDATE', sqlalchemy.Date)

    def _beforeAdd(self):
        self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()

    def _beforeUpdate(self):
        self.modified_date = datetime.datetime.now()

class Service(object):
    def getConf(self,type,rate):
        rate = database.db.query(Conf).filter_by(type=type,rate=rate).first()
        if(rate!=None):
            return rate
        raise Exception(11)