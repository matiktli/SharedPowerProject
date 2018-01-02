from datetime import datetime, date, time,timedelta
import datetime as dt
from config.ConnectorMysql import Connector



class CalendarController:
    PERIOD=4

    def __init__(self):
        self.connector = Connector()
        self.database = self.connector.getDatabase()
        self.cursor = self.database.cursor()

    def saveToolCalendar(self, tool):
        sql = "INSERT INTO CALENDAR(NAME) VALUES ('%s')" % \
              (tool)
        try:
            self.cursor.execute(sql)
            self.database.commit()

        except:
            self.database.rollback()

    def addDayToTableCalendar(self, day):
        if(day == self.lastDate()):
            print("DATE ALREADY EXIST")
            return
        elif(day < self.lastDate()):
            print("U CAN NOT GO BACK IN TIME")
            return
        sql="ALTER TABLE CALENDAR ADD COLUMN \
          `%s` CHAR(20) NOT NULL DEFAULT 'FREE'" % (day)
        try:
            print(sql)
            self.cursor.execute(sql)
            self.database.commit()
        except:
            self.database.rollback()

    def getAllColumns(self):
        sql = "DESCRIBE CALENDAR"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        tab = []
        for row in result:
            tab.append(row[0])
        tab.remove("NAME")
        return tab

    def lastDate(self):
        tab=self.getAllColumns()
        last=tab[len(tab)-1]
        lastDate=datetime.strptime(last,"%Y-%m-%d").date()
        return lastDate

    def updateCalendar(self):
        tmp=dt.date.today()
        last=self.lastDate()
        dif=(last-tmp).days
        daysToAdd=self.PERIOD-dif-1
        for i in range(0,daysToAdd):
            self.addDayToTableCalendar(last+timedelta(i+1))

    def getCalendarForTool(self, tool):
        sql="SELECT * FROM CALENDAR WHERE NAME = '%s'" % tool.name
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        types=list(result)
        types.remove(tool.name)
        dates=self.getAllColumns()
        mapList={} # DATE : TYPE
        counter=0
        for i in dates:
            mapList[dates[counter]]=(types[counter])
            counter += 1
        import operator
        return sorted(mapList.items(),key=operator.itemgetter(0))

    def bookToolForDate(self, tool, dateToBook, userName):
        sql = """UPDATE CALENDAR SET `%s` = "%s" WHERE NAME='%s';\nCOMMIT;""" % (dateToBook,userName,tool.name)
        self.cursor.execute(sql)

