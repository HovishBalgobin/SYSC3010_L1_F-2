from Database import *
from Thingspeak import *
import RPi.GPIO as GPIO
import time
from datetime import date
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
print("Enter Minimum RoomTemp: ")
mintemp = input()
mintemp = int(mintemp)
print("Enter Maximum RoomTemp: ")
maxtemp = input()

maxtemp = int(maxtemp)+1

entry_id = get_entry_id()
print(entry_id)

new_entry_id = entry_id + 1

#datapoint_id = 1
#event_id = 1

#create_data_log(dbconn)
#create_event_log(dbconn)
while True:
    entry_id = get_entry_id()
    alert = False
    if entry_id >= new_entry_id:
        alert = True
        entry_id +=1
        new_entry_id +=1
   
    result2 = read2()
    
    result3 = read3()
#    print(result3)
    
    date = date.today()
    if not alert:
        
        insertUserTable(dbconn,float(result2),float(result3[2]),float(result3[0]),float(result3[1]))
        #datapoint_id += 1
    else:
        result1 = read1()
        
        insertUserTable2(dbconn,result1[1],1)
        #event_id += 1
    if(int(result2) in range(mintemp,maxtemp)):
        pass
    else:
        
        GPIO.output(7, True)
        GPIO.output(11, True)
        time.sleep(15)
        GPIO.output(7, False)
        GPIO.output(11, False)
        print("The temperature is too low or too high")
        
    time.sleep(10)
    
GPIO.cleanup()

