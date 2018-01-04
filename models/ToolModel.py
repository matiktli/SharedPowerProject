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
        self.toolController = ToolController()
        self.calendarController = CalendarController()
        self.userController = UserController()


    def __str__(self):
        return "Name: {0}, Owner: {1}, Price_day: {2}, Price_half: {3}".format(self.name,self.owner,self.priceDay,self.priceHalf)

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
            charge=self.priceDay*days
            newCharge=self.userController.getUserCurrentCharge(userName)+charge
            self.userController.addChargeForUser(newCharge,userName)
        else:
            print("BOOKING LIMIT UP TO 3 DAYS")

    def giveBack(self, returningDate,userName):
        cal=self.getCalendar()
        datesForUser=[]
        for i in range(0,cal.__len__()):
            if cal[i][1] == userName:
                datesForUser.append(cal[i][0])
        lastDate=datetime.strptime(datesForUser[datesForUser.__len__()-1],'%Y-%m-%d').date()
        dif=(returningDate-lastDate).days
        if dif > 0:
            extraCharge=dif*self.priceDay*2
            newCharge = self.userController.getUserCurrentCharge(userName) + extraCharge
            self.userController.addChargeForUser(newCharge, userName)