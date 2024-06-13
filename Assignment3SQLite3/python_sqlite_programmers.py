import sqlite3

# database file connection 
database = sqlite3.connect("assignment3.db")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor()

# Add two students to the database
sql_command = """INSERT INTO STUDENT VALUES(10011, 'Jon', 'Binder', 2025, 'BSCE', 'binderj')"""
cursor.execute(sql_command)

sql_command = """INSERT INTO STUDENT VALUES(10012, 'Carson', 'Mershon', 2035, 'BSCE', 'mershonc')"""
cursor.execute(sql_command)

# Remove an Instructor from the database
sql_command = """DELETE FROM INSTRUCTOR WHERE ID = 20002"""
cursor.execute(sql_command)

# Update an Admin in the database
sql_command = """UPDATE ADMIN SET TITLE = 'Vice-President' WHERE ID = 30002"""
cursor.execute(sql_command)

# SQL command to create a table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS COURSE (  
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
TIME INTEGER,
DAYOFWEEK TEXT,
SEMESTER TEXT,
YEAR INTEGER,
CREDITS INTEGER);"""

# execute the statement 
cursor.execute(sql_command)

# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME) 
VALUES(40001, 'ADVANCED DIGITAL CIRCUIT DESIGN', 'BSCO', 0800);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME)
VALUES(40002, 'ADVANCED ANALOG CIRCUIT DESIGN', 'BSEE', 1300);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME)
VALUES(40003, 'ENGLISH 0.5', 'HUSS', 1500);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME)
VALUES(40004, 'CAD AND CAM', 'BSME', 1650);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME)
VALUES(40005, 'CHEMISTRY', 'BSAS', 0930);"""
cursor.execute(sql_command)

# QUERY FOR ALL
print("Entire table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()

for i in query_result:
    print(i)

# QUERY FOR SOME
print("Classes that are too early for me")
cursor.execute("""SELECT * FROM COURSE WHERE TIME < 1200""")
query_result = cursor.fetchall()

for i in query_result:
    print(i)

# ADDING FROM USER INPUT
crnid = "01326"
title = input("Course Title: ")
dept = input("Course Department: ")

cursor.execute("""INSERT INTO COURSE (CRN, TITLE, DEPARTMENT) VALUES('%s', '%s', '%s');""" % (crnid, title, dept))

print("Entire table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()

for i in query_result:
    print(i)

# Match Instructors to Courses
print("Matching Instructors to Courses")
query = """SELECT c.TITLE, c.DEPARTMENT, i.NAME, i.SURNAME, i.DEPT
FROM COURSE c
JOIN INSTRUCTOR i ON c.DEPARTMENT = i.DEPT"""

cursor.execute(query)
match_result = cursor.fetchall()

if match_result:
    for i in match_result:
        print(i)
else:
    print("No matches found")

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit()

# close the connection 
database.close()
