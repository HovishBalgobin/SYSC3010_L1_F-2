from Database import *
from Thingspeak import *
import RPi.GPIO as GPIO
import time
from Alerts import *


global mintemp, maxtemp, minHum, maxHum, maxAcc;

mintemp = 20
maxtemp = 35
minHum = 20
maxHum = 40
maxAcc = 0.4


def modify_parameters(mintemp1,maxtemp1,minHum1,maxHum1):
    
    
    mintemp=mintemp1
    maxtemp=maxtemp1
    minHum=minHum1
    maxHum=maxHum1
    
    print(mintemp)
    print(maxtemp)
    print(minHum)
    print(maxHum)



global pollingEnabled

def stopPolling():
    pollingEnabled = False

def dataPolling(dbconn):
    pollingEnabled = True
    #print("Enter Minimum RoomTemp: ")
    #mintemp = input()
    #mintemp = int(mintemp)
    #print("Enter Maximum RoomTemp: ")
    #maxtemp = input()

    #maxtemp = int(maxtemp)+1

    entry_id = get_entry_id()
    #print(entry_id)


    #datapoint_id = 1
    #event_id = 1

    #create_data_log(dbconn)
    #create_event_log(dbconn)
    while pollingEnabled:
        alert_level = "None"
        activateFan = False
        gasDetected = False
        soundDetected = False
        
        new_entry_id = get_entry_id()
        if new_entry_id >= entry_id:
            
            result1 = read1(new_entry_id - entry_id)
            entry_id = new_entry_id
            
        result2 = read2()
        
        result3 = read3()
    #    print(result3)
        
        insertUserTable(dbconn,float(result2),float(result3[2]),float(result3[0]),float(result3[1]))
        last_entry_id = int(getLastDataEntries(dbconn, 1)[0][0]) # TODO
        
        
        if(int(result2) < mintemp or int(result2) > maxtemp or float(result3[0]) < mintemp or float(result3[0]) > maxtemp): 
            insertUserTable2(dbconn,'TempAlert',last_entry_id)
            alert_level = "Low"
        
        if (float(result3[1]) < minHum or float(result3[1]) > maxHum): #Humidity
            insertUserTable2(dbconn,'HumidityAlert',last_entry_id)
            alert_level = "Low"
            activateFan = True
        
        if (float(result3[2]) > maxAcc): # Motion
            insertUserTable2(dbconn,'MovementAlert',last_entry_id)
            write1("Action")
            alert_level = "Low"

        if (soundDetected): # Sound
            alert_level = "Low"
        
        if (gasDetected): # Gas 
            alert_level = "High"
            activateFan = True
        
        
        if (alert_level == 'Low'):
            low_alert()
        elif (alert_level == 'High'):
            high_alert()
        
        if (activateFan):
            write2("FanOn")
            time.sleep(5)
            write2("FanOff")
            
        
        time.sleep(1)
        
    

if __name__ == '__main__':
    dbconn = create_connection("")
    dataPolling(dbconn)
    