from config.ConnectorMysql import Connector

#TODO: ALL CLASS
from models.ToolModel import Tool


class ToolController:
    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def saveToolToDatabase(self, tool):

        toolDatabaseObject="INSERT INTO TOOLS(NAME,  \
                           OWNER, PRICE_DAY, PRICE_HALF) \
                            VALUES ('%s','%s','%f','%f')" % \
                           (tool.name,tool.owner,tool.priceDay,tool.priceHalf)
        try:
            self.cursor.execute(toolDatabaseObject)
            self.database.commit()
            print("Tool: {0}_{1} saved to database".format(tool.name,tool.owner))
            self.database.close()
        except:
            self.database.rollback()
            print("ERROR! while saving a tool to db")
            self.database.close()

    def deleteToolFromDatabase(self, tool):
        sql="DELETE FROM TOOLS WHERE NAME = '%s'" % (tool.name)
        try:
            self.cursor.execute(sql)
            print("Tool {0} deleted from database".format(tool.name))
            self.database.commit()
        except:
            self.database.rollback()
            print("ERROR! while deleting tool")

    def findAllTools(self):
        tools=[]
        sql="SELECT * FROM TOOLS"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            tool=Tool(row[0],row[1],row[2],row[3])
            tools.append(tool)
        return tools

    def findTool(self, toolName):
        sql = "SELECT * FROM TOOLS WHERE NAME = '%s'" % toolName
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            tool = Tool(row[0], row[1], row[2], row[3])
        return tool

x=ToolController()
#y=Tool("y","mati",20.1,12.2)
#x.saveToolToDatabase(y)
x.findAllTools()
