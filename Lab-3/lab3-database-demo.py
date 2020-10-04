#!/usr/bin/env python3
import sqlite3
#some initial data
date = '2020-10-04';
time=  '5:03 PM'
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

 sql_create_sensors_table = """CREATE TABLE IF NOT EXISTS sensors (
                                    sesorID integer PRIMARY KEY,
                                    type text NOT NULL,
                                    zone text NOT NULL,
                                    FOREIGN KEY (zone) REFERENCES temps (zone)
                                );"""

cursor.execute('''insert into sensors  values (1, "door", 'kitchen')''');
cursor.execute('''insert into sensors  values (2, "temperature", 'kitchen')''');  
cursor.execute('''insert into sensors  values (3, "door", 'garage')''');  
cursor.execute('''insert into sensors  values (4, "motion", 'garage')''');  
cursor.execute('''insert into sensors  values (5, "temperature", 'garage')''');
 


for i in range(10):
    #execute insert statement
    cursor.execute('''insert into temps values (?, ?)''',
    (date, time));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT type FROM sensors WHERE zone="kitchen" ');
#print data
for row in cursor:
    print(row['type'])
cursor.execute('SELECT * from sensors WHERE type="door"');
for row in cursor:
    print (row['sensorID'],row['type'],row['zone'])
#close the connection
dbconnect.close();
