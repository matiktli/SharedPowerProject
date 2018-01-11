from models.controllers.UserController import UserController


class User:

    def __init__(self,name, password):
        self.name = name
        self.password = password
        self.charge=0

    def __str__(self):
        return "NAME: {0}, PSW: {1}, CHARGE: {2}".format(self.name, self.password, self.charge)

    def create(self, name, password):
        self.name = name
        self.password = password
        return self

    def saveUser(self):
        UserController().saveUserToDatabase(self)
        return self

    def addCharge(self, charge):
        self.charge=self.charge+charge








