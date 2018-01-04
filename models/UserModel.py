from models.controllers.UserController import UserController


class User:

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.charge=0

    def __str__(self):
        return "NAME: {0}, EMAIL: {1}, PSW: {2}".format(self.name,self.email,self.password)

    def create(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        return self

    def saveUser(self):
        UserController().saveUserToDatabase(self)
        return self

    def addCharge(self, charge):
        self.charge=self.charge+charge








