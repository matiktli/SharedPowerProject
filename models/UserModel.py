from models.controllers.UserController import UserController


class User:

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.owned = []
        self.lented = []  # to someone
        self.borrowed = []  # form someone



    def create(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.owned = []
        self.lented = []  # to someone
        self.borrowed = []  # form someone
        return self

    def saveUser(self):
        x= UserController().saveUserToDatabase(self)
        print("")
        return self

    def __str__(self):
        return "NAME: {0}, EMAIL: {1}, PSW: {2}".format(self.name,self.email,self.password)

    def addToOwned(self,tool):
        self.owned.append(tool)





