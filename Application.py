from config.DatabaseCreator import DatabaseCreator

#TABLE GENERATOR
#-----------------
creator=DatabaseCreator()
creator.dropTableUsers()
creator.dropTableTools()
creator.createTableUsers()
creator.createTableTools()
creator.fillTableUsers()
creator.fillTableTools()
#-----------------



#END
#---------------
