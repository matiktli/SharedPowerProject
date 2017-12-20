from models.UserModel import User
from models.controllers.UserController import UserController
from config.DatabaseCreator import DatabaseCreator
#TABLE CONFIG
#-----------------
creator=DatabaseCreator()
#creator.dropTables()
#creator.createTables()
#creator.fillTables()

#-----------------


user = User("elo","kupa","zupa")
user.saveUser()
tab=UserController().findAllUsers()



#END
#---------------
