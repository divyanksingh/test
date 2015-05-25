import MySQLdb
##This is table EMPLOYEE created in TESTDB database: we will work on it
##+------------+-----------+-----+-----+----------+
##| FIRST_NAME | LAST_NAME | AGE | SEX | INCOME   |
##+------------+-----------+-----+-----+----------+
##| ABHINAV    | KUMAR     |  25 | M   |   700000 |
##| GYANENDRA  | KUMAR     |  25 | M   |   600000 |
##| jai        | reddy     |  63 | F   |    98989 |
##| MAYANK     | CHAUHAN   |  23 | M   |  1200000 |
##| PAWAN      | PUNDIR    |  28 | M   |   800000 |
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
sql = '''UPDATE EMPLOYEE SET AGE = AGE + 10
                          WHERE SEX = "%c"; ''' % ('M')
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
##| ABHINAV    | KUMAR     |  35 | M   |   700000 |
##| GYANENDRA  | KUMAR     |  35 | M   |   600000 |
##| jai        | reddy     |  63 | F   |    98989 |
##| MAYANK     | CHAUHAN   |  33 | M   |  1200000 |
##| PAWAN      | PUNDIR    |  38 | M   |   800000 |
##| PREETI     | PUNDIR    |  23 | F   | 12000000 |
##| PREMA      | AJR       |  43 | F   |   120000 |
##| sonal      | raghav    |  43 | F   |   898999 |
##| srutiza    | mohanty   |  33 | F   |  1290000 |
##+------------+-----------+-----+-----+----------+
