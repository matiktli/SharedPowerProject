from datetime import datetime, date, time,timedelta
import datetime as dt

import config.ConnectorMysql
from config.ConnectorMysql import Connector

class DatabaseCreator:
    PERIOD=4
    namesUser = ["mati", "filip", "kasia", "wojtek", "sandra"]
    passwords = ["kulis", "mis", "krzys", "tuptus", "kupa"]
    namesTool=["AA","BB","CC","DD","EE"]
    priceDay=[10.1,11.1,20.5,30.4,50.4]
    priceHalf=[2.2,3.3,4.4,5.5,6.6]


    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def createTableUsers(self):
        usersTable = """CREATE TABLE USERS (
            ID  INT NOT NULL AUTO_INCREMENT,
           NAME  CHAR(20) NOT NULL UNIQUE,
           PASSWORD CHAR(20) NOT NULL,
           CHARGE FLOAT DEFAULT '0.0',
           PRIMARY KEY(ID)
           )"""
        self.cursor.execute(usersTable)

    def dropTableUsers(self):
        sql = "DROP TABLE IF EXISTS USERS"
        self.cursor.execute(sql)

    def createTableTools(self):
        toolsTable= """CREATE TABLE TOOLS ( 
            NAME  CHAR(20) NOT NULL UNIQUE,
            OWNER  CHAR(20) NOT NULL,
            PRICE_DAY  DOUBLE NOT NULL,
            PRICE_HALF  DOUBLE NOT NULL,
            DESCRIPTION CHAR(100) DEFAULT 'SOME DESCRIPTION'
            )"""
        self.cursor.execute(toolsTable)

    def dropTableTools(self):
        sql = "DROP TABLE IF EXISTS TOOLS"
        self.cursor.execute(sql)

    def createTableCalendar(self):
        calendar="CREATE TABLE CALENDAR (NAME CHAR(20) NOT NULL UNIQUE"
        for i in range(0,self.PERIOD):
            calendar+=", `%s` CHAR(20) NOT NULL DEFAULT 'FREE' " % (dt.date.today() + dt.timedelta(i))
        calendar+=")"
        self.cursor.execute(calendar)

    def dropTableCalendar(self):
        sql = "DROP TABLE IF EXISTS CALENDAR"
        self.cursor.execute(sql)

    def fillTableUsers(self):
        for i in range(len(self.namesUser)):
            sql= "INSERT INTO USERS(NAME, PASSWORD) \
            VALUES ('%s', '%s')" % \
                             (self.namesUser[i], self.passwords[i])
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except:
                self.database.rollback()

    def fillTableTools(self):
        for i in range(len(self.namesUser)):

            sql = "INSERT INTO TOOLS(NAME,  \
                    OWNER, PRICE_DAY, PRICE_HALF) \
                    VALUES ('%s','%s','%f','%f')" % \
                                 (self.namesTool[i], self.namesUser[i], self.priceDay[i], self.priceHalf[i])
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except:
                self.database.rollback()

    def fillTableCalendar(self):
        for i in range(len(self.namesUser)):

            sql = "INSERT INTO CALENDAR(NAME) VALUES ('%s')" % \
                                 (self.namesTool[i])
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except:
                self.database.rollback()


