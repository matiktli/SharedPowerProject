from datetime import timedelta, datetime

from models.controllers.CalendarController import CalendarController
from models.controllers.ToolController import ToolController
from models.controllers.UserController import UserController


class Tool():


    def __init__(self,name,owner,priceDay,priceHalf):
        self.id = None
        self.name=name
        self.priceDay=priceDay
        self.priceHalf=priceHalf
        self.owner=owner
        self.description=None
        self.toolController = ToolController()
        self.calendarController = CalendarController()
        self.userController = UserController()


    def __str__(self):
        return "{0}_{1}_{2}_{3}".format(self.name,self.owner,self.priceDay,self.priceHalf)

    def saveToolToDatabase(self):
        self.toolController.saveToolToDatabase(self)
        self.calendarController.saveToolCalendar(self.name)

    def getCalendar(self):
        calendarRow=self.calendarController.getCalendarForTool(self)
        return calendarRow

    def book(self,dateToBook,userName,days=1,type="DAY"):
        if days in range(1,4):
            for i in range(0,days):
                self.calendarController.bookToolForDate(self,dateToBook+timedelta(i),userName,type)
            if type=="HALF":
                charge=self.priceHalf*days
            else:
                charge=self.priceDay*days
            self.userController.addChargeForUser(charge,userName)
            return (charge)
        else:
            print("BOOKING LIMIT UP TO 3 DAYS")
            return None

    def giveBack(self, returningDate,userName):
        cal=self.getCalendar()
        datesForUser=[]
        for i in range(0,cal.__len__()):
            if cal[i][1].lower() == userName+"_day" or cal[i][1].lower() == userName+"_half":
                datesForUser.append(cal[i][0])
                dateToReturn=datetime.strptime(cal[i][0], '%Y-%m-%d').date()
                CalendarController().returnTool(self,dateToReturn)
        lastDate=datetime.strptime(datesForUser[datesForUser.__len__()-1],'%Y-%m-%d').date()
        dif=(returningDate-lastDate).days
        extraCharge=0
        if dif > 0:
            extraCharge=dif*self.priceDay*2
            newCharge = self.userController.getUserCurrentCharge(userName) + extraCharge
            self.userController.addChargeForUser(newCharge, userName)
        else: dif=0
        return (dif, extraCharge)

    def getDescription(self):
        return ToolController().getDescriptionForTool(self.name)

    def setDescription(self,desc):
        ToolController().setDescriptionForTool(self.name,desc)