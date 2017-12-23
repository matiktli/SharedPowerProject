import datetime

from config.DatabaseCreator import DatabaseCreator

#TABLE GENERATOR
#-----------------
from models.ToolModel import Tool
from models.controllers.ToolController import ToolController

creator=DatabaseCreator()
if(True):
    if(True): # DROP
        creator.dropTableCalendar()
        creator.dropTableUsers()
        creator.dropTableTools()
    if(True): #CREATE
        creator.createTableCalendar()
        creator.updateCalendar()
        creator.createTableUsers()
        creator.createTableTools()
    if(True): #FILL
        creator.fillTableCalendar()
        creator.fillTableUsers()
        creator.fillTableTools()

#newTool=Tool("FF","mati",42.2,30.0)
#newTool.saveToolToDatabase()
#newTool2=Tool("GG","kasia",10,7)
#newTool2.saveToolToDatabase()
#-----------------
#toolController=ToolController()
#tools=toolController.findAllToolsForUser("mati")
#print('\n'.join(map(str,tools)))
#creator.addDayToTableCalendar(datetime.date.today()+datetime.timedelta(days=6))
#creator.addDayToTableCalendar(datetime.date.today()+datetime.timedelta(days=-1))
#END
#---------------

