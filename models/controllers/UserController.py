import pymysql

from config.ConnectorMysql import Connector


class UserController:


    def __init__(self):
        self.database=Connector().getDatabase()
        self.cursor = self.database.cursor()
        print("Opening connection to database")

    def saveUserToDatabase(self,user):

        userDatabaseObject = "INSERT INTO USERS(NAME, \
           EMAIL, PASSWORD) \
           VALUES ('%s', '%s' , '%s')" % \
                             (user.name, user.email,user.password)

        try:
            self.cursor.execute(userDatabaseObject)
            self.database.commit()
            print("User {0} saved to database".format(user.name))
            self.database.close()

        except:
            self.database.rollback()
            print("ERROR! User {0} NOT saved to database".format(user.name))
            self.database.close()


    def deleteUserFromDatabase(self, user):
        username=user.name
        #
        print("User {0} deleted from database".format(username))

    def findUser(self, username):
        #
        print("xd")

    def findAllUsers(self):
        users=[]
        sql = "SELECT * FROM USERS"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            name = row[0]
            email = row[1]
            password = row[2]
            from models.UserModel import User
            users.append(User(name,email,password))
        return users