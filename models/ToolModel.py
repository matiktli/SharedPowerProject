import time
from datetime import date, datetime, timedelta

from models.CalendarModel import Calendar
from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController


class Tool:

    toolController=ToolController()
    calendarController=CalendarController()
    def __init__(self,name,owner,priceDay,priceHalf):
        self.id = None
        self.name=name
        self.priceDay=priceDay
        self.priceHalf=priceHalf
        self.owner=owner



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
        calendarRow=self.calendarController.getCalendarForTool(self.name)
        return calendarRow

