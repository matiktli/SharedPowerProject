import pymysql

# Config file for connection to mysql

# Open database connection
# (domain,username,password,database_name)
db = pymysql.connect("localhost","adminSharedPower","password","SharedPower_db" )
# Create cursor object
cursor = db.cursor()
# Execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)
# Disconnect from MySQL server
db.close()