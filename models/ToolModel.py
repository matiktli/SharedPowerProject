from datetime import timedelta

from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController


class Tool():


    def __init__(self,name,owner,priceDay,priceHalf):
        self.id = None
        self.name=name
        self.priceDay=priceDay
        self.priceHalf=priceHalf
        self.owner=owner
        self.toolController = ToolController()
        self.calendarController = CalendarController()


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
        self.toolController.saveToolToDatabase(self)
        self.calendarController.saveToolCalendar(self.name)

    def getCalendar(self):
        calendarRow=self.calendarController.getCalendarForTool(self)
        return calendarRow

    def book(self,dateToBook,userName,days=1):
        if days in range(1,4):
            for i in range(0,days):
                self.calendarController.bookToolForDate(self,dateToBook+timedelta(i),userName)
        else:
            print("BOOKING LIMIT UP TO 3 DAYS")
