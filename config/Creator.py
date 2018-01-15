from config.DatabaseCreator import DatabaseCreator

#TABLE GENERATOR
#-----------------
from models.controllers.CalendarController import CalendarController


class WholeCreator():

    def __init__(self):
        creator=DatabaseCreator()
        calendarController=CalendarController()
        stat=True
        if(stat):
            if(stat): # DROP
                creator.dropTableCalendar()
                creator.dropTableUsers()
                creator.dropTableTools()
                print("Databases DROPED")

            if(stat): #CREATE
                creator.createTableCalendar()
                calendarController.updateCalendar()
                creator.createTableUsers()
                creator.createTableTools()
                print("Databases CREATED")

            if(stat): #FILL
                creator.fillTableCalendar()
                creator.fillTableUsers()
                creator.fillTableTools()
                creator.fillPhotos()
                print("Databases FILLED")
