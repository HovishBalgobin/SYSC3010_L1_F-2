import sqlite3 # import
from sqlite3 import Error

def create_data_log(conn): # creating the first table "DATA_LOG" with the necessary parameters
    Table_string = """CREATE TABLE DATA_LOG (
                                            datapoint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            child_temp float NOT NULL,
                                            crib_acc float NOT NULL,
                                            room_temp float NOT NULL,
                                            room_hum float NOT NULL,
                                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                            );"""
    try:
        cursor = conn.cursor()
        cursor.execute(Table_string)
    except Error as e:
        print(e)
                                         
def create_event_log(conn):  # creating the second table "EVENT_LOG" with the necessary parameters
    Table_string = """ CREATE TABLE EVENT_LOG (
                                           event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                           event_type text NOT NULL,
                                           datapoint_id int,
                                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                           );"""
    try:
        cursor = conn.cursor()
        cursor.execute(Table_string)
    except Error as e:
        print(e)                    

def getLastDataEntries(conn,numberOfEntries): # This function gets the latest data entires that were made into the DATA_LOG table
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM (SELECT * FROM DATA_LOG ORDER BY datapoint_id DESC LIMIT ''' + str(numberOfEntries) + ''') ORDER BY datapoint_id ASC;''');
    conn.commit()
    return cursor.fetchall()

def insertUserTable(conn,child_temp,crib_acc,room_temp,room_hum): # This function inserts parameters and how they should be arranged in the DATA_LOG table
    cursor = conn.cursor()
    cursor.execute('''insert into DATA_LOG(child_temp,crib_acc,room_temp,room_hum) values (?,?,?,?)''',(child_temp,crib_acc,room_temp,room_hum));
    conn.commit()

def insertUserTable2(conn,event_type,datapoint_id): # This function inserts the necessary columns with their parameter into the EVENT_LOG table
    cursor = conn.cursor()
    cursor.execute('''insert into EVENT_LOG(event_type,datapoint_id) values (?,?)''',(event_type,datapoint_id));
    conn.commit()

def create_connection(db_file): # This creates a connection to our database
    conn = None
    try:
        conn = sqlite3.connect("projectdatabase.db") # connecting using the appropriate name of our database
        return conn
    except Error as e:
        print(e)
        
    return conn


    
