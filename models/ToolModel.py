import time
from datetime import date


class Tool:
    def __init__(self,name,priceDay,priceHalf,owner,avaiable = True):
        self.name=name #UNIQUE
        self.priceDay=priceDay
        self.priceHalf=priceHalf
        self.owner=owner
        self.avaiable=avaiable
        # TODO: MAP IS BETTER WAY
        self.calendar=[2][42] # 42 days = 6 weeks

    def getCalendar(self):
        return self.calendar

    def book(self):
        print("")



