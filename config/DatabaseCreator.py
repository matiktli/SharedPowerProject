import config.ConnectorMysql
from config.ConnectorMysql import Connector

class DatabaseCreator:

    namesUser = ["mati", "filip", "kasia", "wojtek", "sandra"]
    emails = ["srati@xx", "tulip@xx", "srasia@xx", "srojtek@xx", "skafandra@xx"]
    passwords = ["kulis", "mis", "krzys", "tuptus", "kupa"]
    namesTool=["AA","BB","CC","DD","EE"]
    priceDay=[10.1,11.1,20.5,30.4,50.4]
    priceHalf=[2.2,3.3,4.4,5.5,6.6]


    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def createTableUsers(self):
        usersTable = """CREATE TABLE USERS (
           NAME  CHAR(20) NOT NULL,
           EMAIL  CHAR(20) NOT NULL,
           PASSWORD CHAR(20) NOT NULL  
           )"""
        self.cursor.execute(usersTable)

    def dropTableUsers(self):
        sql = "DROP TABLE IF EXISTS USERS"
        self.cursor.execute(sql)

    def createTableTools(self):
        toolsTable= """CREATE TABLE TOOLS ( 
            NAME  CHAR(20) NOT NULL,
            OWNER  CHAR(20) NOT NULL,
            PRICE_DAY  DOUBLE NOT NULL,
            PRICE_HALF  DOUBLE NOT NULL
            )"""
        self.cursor.execute(toolsTable)

    def dropTableTools(self):
        sql = "DROP TABLE IF EXISTS TOOLS"
        self.cursor.execute(sql)

    def fillTableUsers(self):
        for i in range(len(self.namesUser)):
            sql= "INSERT INTO USERS(NAME, \
            EMAIL, PASSWORD) \
            VALUES ('%s', '%s' , '%s')" % \
                             (self.namesUser[i], self.emails[i],self.passwords[i])
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