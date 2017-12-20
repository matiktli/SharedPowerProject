import config.ConnectorMysql


class DatabaseCreator:

    def __init__(self):
        self.cursor=config.ConnectorMysql.Connector().getCursor()


    def createTables(self):
        #TODO: if check statement needed
        usersTable = """CREATE TABLE USERS (
           NAME  CHAR(20) NOT NULL,
           EMAIL  CHAR(20) NOT NULL,
           PASSWORD CHAR(20) NOT NULL  
           )"""
        self.cursor.execute(usersTable)

    def dropTables(self):
        sql = "DROP TABLE IF EXISTS USERS"
        self.cursor.execute(sql)

    def fillTables(self):
        print("")