import MySQLdb
import re

# Open database connection
db = MySQLdb.connect(host="localhost",user ="root",passwd = "welcome123",db = "friends")
#NOTE:  THESE details must be set from cmd prompt sql including database name

# prepare a cursor object using cursor() method
cursor = db.cursor()
#check if table exists
# Drop table if it already exist using execute() method.
cursor.execute('show tables;')
data = cursor.fetchall()
#(('dummy',), ('employee',), ('STUDENTent',)) = data !!!table names displayed as small only always....
for elem in data:
    if re.search('^STUDENT$',elem[0],re.I) != None:        
        cursor.execute("DROP TABLE STUDENT")

# Create table as per requirement
sql = """CREATE TABLE STUDENT (
         FIRST_NAME  VARCHAR(20) NOT NULL,
         LAST_NAME  VARCHAR(20),
         AGE INT,  
         SEX CHAR(1),
         MARKS FLOAT,
         PRIMARY KEY(FIRST_NAME));"""

cursor.execute(sql)

cmd = '''INSERT INTO STUDENT(FIRST_NAME,LAST_NAME,AGE,SEX,MARKS)
VALUES("PRETHI","PUNDIR",23,"F",98)'''
try:
   # Execute the SQL command
   cursor.execute(cmd)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
# disconnect from server

###another way of insertion by variables
fname = 'sudipta'
lname = 'basu'
age = 30
sex=  'M'
marks = 99.4
cmd = '''INSERT INTO STUDENT (FIRST_NAME,LAST_NAME,AGE,SEX,MARKS)
VALUES("%s","%s",%d,"%s",%f)''' %(fname,lname,age,sex,marks)
try:
   # Execute the SQL command
   cursor.execute(cmd)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
# disconnect from server
db.close()
########## this will be table output
##mysql> SELECT * FROM STUDENT;
##+------------+-----------+------+------+-------+
##| FIRST_NAME | LAST_NAME | AGE  | SEX  | MARKS |
##+------------+-----------+------+------+-------+
##| PRETHI     | PUNDIR    |   23 | F    |    98 |
##| sudipta    | basu      |   30 | M    |  99.4 |
##+------------+-----------+------+------+-------+
##2 rows in set (0.00 sec)
