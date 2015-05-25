import MySQLdb
##This is table EMPLOYEE created in TESTDB database: we will work on it
##+------------+-----------+-----+-----+----------+
##| FIRST_NAME | LAST_NAME | AGE | SEX | INCOME   |
##+------------+-----------+-----+-----+----------+
##| ABHINAV    | KUMAR     |  45 | M   |   700000 |
##| GYANENDRA  | KUMAR     |  45 | M   |   600000 |
##| jai        | reddy     |  63 | F   |    98989 |
##| MAYANK     | CHAUHAN   |  43 | M   |  1200000 |
##| PAWAN      | PUNDIR    |  48 | M   |   800000 |
##| PREETI     | PUNDIR    |  23 | F   | 12000000 |
##| PREMA      | AJR       |  43 | F   |   120000 |
##| sonal      | raghav    |  43 | F   |   898999 |
##| srutiza    | mohanty   |  33 | F   |  1290000 |
##+------------+-----------+-----+-----+----------+


# Open database connection
db = MySQLdb.connect(host="localhost",user ="root",passwd = "welcome123",db = "friends")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#Prepare SQL query to UPDATE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (40)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   
# disconnect from server
db.close()
#see output
##+------------+-----------+-----+-----+----------+
##| FIRST_NAME | LAST_NAME | AGE | SEX | INCOME   |
##+------------+-----------+-----+-----+----------+
##| PREETI     | PUNDIR    |  23 | F   | 12000000 |
##| srutiza    | mohanty   |  33 | F   |  1290000 |
##+------------+-----------+-----+-----+----------+
