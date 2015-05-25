import MySQLdb
##host: name of system where MySQL is running. Default is localhost.
##{ user: user id. Default value = current user
##{ passwd: password for user id. No default value
##{ db: database that you want to connect to. No default value
##{ port: port where server is on. Default value is 3306

# Open database connection
db = MySQLdb.connect(host="localhost",user ="root",passwd = "welcome123",db = "friends" )

# prepare a cursor object using cursor() method
#Creating a cursor enables you to make queries through python. It is also
#where data is kept once a query is executed.
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
