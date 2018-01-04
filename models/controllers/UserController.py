import pymysql

from config.ConnectorMysql import Connector



class UserController:



    def __init__(self):
        self.database = Connector().getDatabase()
        self.cursor = self.database.cursor()

    def saveUserToDatabase(self,user):

        userDatabaseObject = "INSERT INTO USERS(NAME, \
           EMAIL, PASSWORD) \
           VALUES ('%s', '%s' , '%s')" % \
                             (user.name, user.email,user.password)

        try:
            self.cursor.execute(userDatabaseObject)
            self.database.commit()
            print("User {0} saved to database".format(user.name))

        except:
            self.database.rollback()
            print("ERROR! User {0} NOT saved to database".format(user.name))


    def deleteUserFromDatabase(self, user):
        sql = "DELETE FROM USERS WHERE NAME = '%s'" % (user.name)
        try:
            self.cursor.execute(sql)
            self.database.commit()
            print("User {0} deleted from database".format(user.name))
        except:
            self.database.rollback()
            print("ERROR! while deleting user")


    def findUser(self, username):
        sql = "SELECT * FROM USERS WHERE NAME = '%s'" % (username)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            name=row[0]
            email=row[1]
            password=row[2]
            charge=row[3]
            from models.UserModel import User
            user = User(name,email,password)
            user.addCharge(charge)
        return user


    def findAllUsers(self):
        users=[]
        sql = "SELECT * FROM USERS"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            name = row[0]
            email = row[1]
            password = row[2]
            charge = row[3]
            from models.UserModel import User
            user = User(name, email, password)
            user.addCharge(charge)
            users.append(user)
        return users

    def getUserCurrentCharge(self, username):
        sql = "SELECT CHARGE FROM USERS WHERE NAME = '%s'" % username
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            return row[0]

    def addChargeForUser(self,charge,username):
        sql = """UPDATE USERS SET CHARGE = %s WHERE NAME='%s'""" % (charge,username)
        self.cursor.execute(sql)
        self.database.commit()
