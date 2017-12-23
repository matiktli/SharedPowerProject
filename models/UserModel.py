from models.controllers.UserController import UserController


class User:

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.owned = []
        self.lented = []  # to someone
        self.borrowed = []  # form someone

    def __str__(self):
        return "NAME: {0}, EMAIL: {1}, PSW: {2}".format(self.name,self.email,self.password)

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
        return self

    def addToOwned(self,tool):
        self.owned.append(tool)





