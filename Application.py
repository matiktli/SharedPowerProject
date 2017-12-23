from config.DatabaseCreator import DatabaseCreator

#TABLE GENERATOR
#-----------------
from models.ToolModel import Tool
from models.controllers.ToolController import ToolController

creator=DatabaseCreator()
creator.dropTableCalendar()
creator.createTableCalendar()
creator.fillTableCalendar()
creator.dropTableUsers()
creator.dropTableTools()
creator.createTableUsers()
creator.createTableTools()
creator.fillTableUsers()
creator.fillTableTools()
newTool=Tool("FF","mati",42.2,30.0)
newTool.saveToolToDatabase()
newTool2=Tool("GG","kasia",10,7)
newTool2.saveToolToDatabase()
#-----------------
toolController=ToolController()
tools=toolController.findAllToolsForUser("mati")
print('\n'.join(map(str,tools)))

#END
#---------------
