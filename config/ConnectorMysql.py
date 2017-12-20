import pymysql


class Connector:

    def __init__(self):
        # Open database connection
        # (domain,username,password,database_name)
        self.db = pymysql.connect("localhost","adminSharedPower","password","SharedPower_db" )
        # Create cursor object
        self.cursor = self.db.cursor()



    # Function returning cursor for db
    def getCursor(self):
        return self.cursor

    def getDatabase(self):
        return self.db

    def disconnect(self):
        print("LOG: Disconnected from database")
        self.db.close()