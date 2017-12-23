import time
from datetime import date, datetime, timedelta

from models.CalendarModel import Calendar
from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController


class Tool:
    def __init__(self,name,owner,priceDay,priceHalf):
        self.id = None
        self.name=name
        self.priceDay=priceDay
        self.priceHalf=priceHalf
        self.owner=owner
        self.calendar=Calendar(self.name)
        # Creating two dimensional array...
        w, h = 42, 2;
        self.calendar = [[0 for x in range(w)] for y in range(h)]
        # 42 days = 6 weeks
        for i in range(0,41):
            self.calendar[0][i]=datetime.today().date() + timedelta(i)
            self.calendar[1][i]=True

    def __str__(self,list=None):
        formater = "Name: {0}, Owner: {1}, Price_day: {2}, Price_half: {3}".format(self.name,self.owner,self.priceDay,self.priceHalf)
        result=None
        if list:
            for row in list:
                result += "Name: {0}, Owner: {1}, Price_day: {2}, Price_half: {3} \n".format(row[0],row[1],row[2],row[3])
            return result
        else:
            return formater

    def saveToolToDatabase(self):
        ToolController().saveToolToDatabase(self)
        CalendarController().saveToolCalendar(self.name)




    def printCalendar(self):
        for i in range(0, 41):
            print("Date: {0} -> {1} ".format(self.calendar[0][i], self.calendar[1][i]))

    def getCalendar(self):
        return self.calendar

    def checkDate(self,dateToCheck):
        flaga=False
        index=-1
        for i in range(0,41):
            if (self.calendar[0][i]) == dateToCheck:
                    index=i
        if(index > -1):
            if(self.calendar[1][index]==True):
                return True
            else: return False
        else:return False



    def book(self, user, dateToBook):
        if self.checkDate(dateToBook):
            self.calendar[1][self.calendar[0].index(dateToBook)]=user
            print("Boked for {0} on date: {1}".format(user,dateToBook.__str__()))
            return True
        else:
            print("Error while booking")
            return False





#x=Tool("xd",10,7,"mati")
#calendar=x.getCalendar()
#x.printCalendar()
#datka = (datetime.today()+timedelta(days=10)).date()
#print(datka)
#print(x.checkDate(datka))
#x.book("ktos",datka)
