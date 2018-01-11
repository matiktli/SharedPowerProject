import datetime

from config.DatabaseCreator import DatabaseCreator

#TABLE GENERATOR
#-----------------
from models.ToolModel import Tool
from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController

creator=DatabaseCreator()
calendarController=CalendarController()
stat=True
if(stat):
    print("Databases reset")
    if(stat): # DROP
        creator.dropTableCalendar()
        creator.dropTableUsers()
        creator.dropTableTools()
    if(stat): #CREATE
        creator.createTableCalendar()
        calendarController.updateCalendar()
        creator.createTableUsers()
        creator.createTableTools()
    if(stat): #FILL
        creator.fillTableCalendar()
        creator.fillTableUsers()
        creator.fillTableTools()
    if(stat): #ADD NEW & BOOK
        newTool=Tool("FF","mati",10,5)
        newTool.saveToolToDatabase()
        newTool.book(datetime.date.today(),'KASIA',2)
        newTool.giveBack(datetime.date.today()+datetime.timedelta(0),'KASIA')
        newTool2 = Tool("GG", "sratka", 100, 50)
        newTool2.saveToolToDatabase()
        newTool2.book(datetime.date.today(),'KASIA',1)


