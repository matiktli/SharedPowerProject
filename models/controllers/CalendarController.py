from config.ConnectorMysql import Connector


class CalendarController:

    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def saveToolCalendar(self, tool):
        sql = "INSERT INTO CALENDAR(NAME) VALUES ('%s')" % \
              (tool)
        try:
            self.cursor.execute(sql)
            self.database.commit()

        except:
            self.database.rollback()

