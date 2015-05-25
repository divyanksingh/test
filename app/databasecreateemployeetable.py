import MySQLdb
import re
#aim to create this table
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
print "welcome to database creation"
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
    if re.search('^EMPLOYEE$',elem[0],re.I) != None:        
        cursor.execute("DROP TABLE EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  VARCHAR(20) NOT NULL,
         LAST_NAME  VARCHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT,
         PRIMARY KEY(FIRST_NAME));"""

cursor.execute(sql)

mydict = {'ABHINAV':['KUMAR',25,'M',700000],
          'GYANENDRA':['KUMAR',25,'M',600000],
          'jai':['reddy',63,'F',98989],
          'MAYANK':['CHAUHAN',23,'M',1200000],
          'PAWAN':['PUNDIR',28,'M',800000],
          'PREETI':['PUNDIR',23,'F',12000000],
          'PREMA':['AJR',43,'F',120000],
          'sonal':['raghav',43,'F',898999],
          'srutiza':['mohanty',33,'F',1290000],
          'monkey':['pandey',53,'M',1000000]
          }


for k,v in mydict.items():    
    cmd = '''INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
    VALUES("%s","%s",%d,"%s",%f)''' %(k,v[0],v[1],v[2],v[3])
    
    try:
       # Execute the SQL command
       cursor.execute(cmd)
       # Commit your changes in the database
       db.commit()0
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
