import sqlalchemy.orm
import sqlalchemy.ext.declarative
import os,sys

os.environ['path']= os.getcwd()+os.altsep+'lib'+os.altsep+sys.platform

engine = sqlalchemy.create_engine('oracle://bigcus:bigcus@192.168.50.75:1521/bosdb', echo=True)
db = sqlalchemy.orm.sessionmaker(bind=engine)()
model = sqlalchemy.ext.declarative.declarative_base()

class Action(object):
    def _beforeAdd(self):
        return False

    def _afterAdd(self):
        return False

    def add(self):
        db.add(self)
        self._beforeAdd()
        db.commit()
        self._afterAdd()

    def _beforeUpdate(self):
        return False

    def _afterUpdate(self):
        return False

    def update(self):
        self._beforeUpdate()
        db.commit()
        self._afterUpdate()