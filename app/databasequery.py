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

# Prepare SQL query to INSERT a record into the database.
sql = '''SELECT * FROM EMPLOYEE 
       WHERE INCOME > %d ''' % (1200000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a tuple of tuples
   results = cursor.fetchall() 
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
