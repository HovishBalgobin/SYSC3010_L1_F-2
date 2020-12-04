import sqlite3
from sqlite3 import Error

def create_data_log(conn):
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
                                         
def create_event_log(conn):
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



def insertUserTable(conn,child_temp,crib_acc,room_temp,room_hum):
    cursor = conn.cursor()
    cursor.execute('''insert into DATA_LOG(child_temp,crib_acc,room_temp,room_hum) values (?,?,?,?)''',(child_temp,crib_acc,room_temp,room_hum));
    conn.commit()

def insertUserTable2(conn,event_type,datapoint_id):
    cursor = conn.cursor()
    cursor.execute('''insert into EVENT_LOG(event_type,datapoint_id) values (?,?)''',(event_type,datapoint_id));
    conn.commit()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect("projectdatabase.db")
        return conn
    except Error as e:
        print(e)
        
    return conn


    
