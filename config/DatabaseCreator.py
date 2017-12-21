import config.ConnectorMysql


class DatabaseCreator:

    def __init__(self):
        self.cursor=config.ConnectorMysql.Connector().getCursor()


    def createTableUsers(self):
        #TODO: if check statement needed
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

x=DatabaseCreator()
x.createTableTools()