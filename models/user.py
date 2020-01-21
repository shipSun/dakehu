import datetime

class User(object):
    id =1
    price = 1

    _rate = None

    def setRate(self,rate):
        self._rate = rate

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return (self.price*self._rate.multiply)/100

class _AveragePrice(object):
    index = '202001'
    price = '10.00'
    create_date = '2020-01-01 00:00:00'

class _AveragePriceService(object):
    @staticmethod
    def getAveratePrice(index):
        averagePrice = _AveragePrice()
        return averagePrice

    @staticmethod
    def getIndex():
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        return last_month.strftime("%Y%m")

class Service(object):
    _AveragePrice = None

    def getAveragePriceByInPrice(self,rate):
        if(self._AveragePrice==None):
            self._AveragePrice = _AveragePriceService.getAveratePrice(_AveragePriceService.getIndex())

        return self._AveragePrice