from models.UserModel import User
from models.controllers.UserController import UserController
from config.DatabaseCreator import DatabaseCreator
#TABLE CONFIG
#-----------------
#creator=DatabaseCreator()
#creator.dropTables()
#creator.createTables()
#creator.fillTables()

#-----------------


user = User("mati","adfasf","aswww")
user.saveUser()
#tab=UserController().findAllUsers()
#user2=tab[1]
#print(user2)
user2 = UserController().findUser("mati")
print(user2)
UserController().deleteUserFromDatabase(user2)


#END
#---------------
