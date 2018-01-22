from config.DatabaseCreator import DatabaseCreator
from models.controllers.CalendarController import CalendarController


class WholeCreator():

    def __init__(self):
        creator=DatabaseCreator()
        calendarController=CalendarController()
        calendarController.PERIOD=int(input("What is the PERIOD? \n"))
        stat=True
        if(stat):
            if(stat): # DROP
                creator.dropTableCalendar()
                creator.dropTableUsers()
                creator.dropTableTools()
                print("Databases DROPED")
                input("Press Enter to continue...")

            if(stat): #CREATE
                creator.createTableCalendar()
                calendarController.updateCalendar()
                creator.createTableUsers()
                creator.createTableTools()
                print("Databases CREATED")
                input("Press Enter to continue...")

            if(stat): #FILL
                creator.fillTableCalendar()
                creator.fillTableUsers()
                creator.fillTableTools()
                creator.fillPhotos()
                print("Databases FILLED")
                input("Press Enter to continue...")