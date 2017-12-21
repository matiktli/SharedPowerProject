from config.ConnectorMysql import Connector

#TODO: ALL CLASS
class ToolController:
    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def saveToolToDatabase(self, tool):

        toolDatabaseObject=""

        try:
            self.cursor.execute(toolDatabaseObject)
            self.database.commit()
            self.database.close()
        except:
            self.database.rollback()
            self.database.close()

    def deleteToolFromDatabase(self, tool):

        sql="DELETE FROM ..."

        try:
            self.cursor.execute(sql)
            self.database.commit()
        except:
            self.database.rollback()

    def findTool(self, id):
        sql=""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            p1=row[0]
            #....
            #....
            #tool = Tool()
        #return