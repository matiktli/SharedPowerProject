import pymysql


class Connector:

    def __init__(self):
        # Open database connection
        # (domain,username,password,database_name)
        self.db = pymysql.connect("localhost","adminSharedPower","password","SharedPower_db" )
        # Create cursor object
        self.cursor = self.db.cursor()
        # execute SQL query using execute() method.
        self.cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)



    # Function returning cursor for db
    def getCursor(self):
        return self.cursor

    def getDatabase(self):
        return self.db

    def disconnect(self):
        print("LOG: Disconnected from database")
        self.db.close()