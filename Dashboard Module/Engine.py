from Database import * # import functions in Database.py
from Thingspeak import * # import functions in Thingspeak.py
import RPi.GPIO as GPIO
import time
from Alerts import * # import functions in Alerts.py
from email_notif import email_alert


global mintemp, maxtemp, minHum, maxHum, maxAcc; # making global variables

# assigning numbers (thresholds) for the variables
mintemp = 0
maxtemp = 100
minHum = 20
maxHum = 40
maxAcc = 0.4


def modify_parameters(mintemp1,maxtemp1,minHum1,maxHum1): # function to modify the parameters
    
     
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
    pollingEnabled = False # fucntion that stops polling

def dataPolling(dbconn, recipient_email): # function to poll data from the database
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
    while pollingEnabled: # while loop that runs as long as data polling is occurring
        alert_types = []
        alert_level = "None"
        activateFan = False
        gasDetected = False
        soundDetected = False
        
        new_entry_id = get_entry_id()
        if new_entry_id >= entry_id:
            
            result1 = read1(new_entry_id - entry_id) #assign result 1 to read function
            entry_id = new_entry_id
            
            if ('GasAlert' in result1):
                gasDetected = True
                insertUserTable2(dbconn,'GasAlert',0) #if we have a 'GasAlert' we insert it into table 2 which is the EVENT_LOG table
            
            if ('SoundAlert' in result1):
                soundDetected = True
                insertUserTable2(dbconn,'SoundAlert',0) # if we have a 'SoundAlert' it is also inserted into the EVENT_LOG table
            
        result2 = read2() # assigning result2 to read2 function from Thingspeak.py
        
        result3 = read3() # assigning result3 to read3 function from Thingspeak.py
    #    print(result3)
    
        
        
        
        insertUserTable(dbconn,float(result2),float(result3[2]),float(result3[0]),float(result3[1]))
        last_entry_id = int(getLastDataEntries(dbconn, 1)[0][0]) # TODO
        
        
        if(float(result2) < mintemp or float(result2) > maxtemp or float(result3[0]) < mintemp or float(result3[0]) > maxtemp): 
            insertUserTable2(dbconn,'TempAlert',last_entry_id)
            alert_types.append("Temperature Alert")
            alert_level = "Low" # setting the alert level for a temperature alert as a low level alert
        
        if (float(result3[1]) < minHum or float(result3[1]) > maxHum): #Humidity
            insertUserTable2(dbconn,'HumidityAlert',last_entry_id)
            alert_types.append("Humidity Alert")
            alert_level = "Low" # Setting alert level for a humidity alert to a low alert
            activateFan = True
        
        if (float(result3[2]) > maxAcc): # Motion
            insertUserTable2(dbconn,'MovementAlert',last_entry_id)
            alert_types.append("Movement Alert")
            write1("Action")
            alert_level = "Low" # Setting alert level for a movement alert to low

        if (soundDetected): # Sound
            alert_types.append("Loud Sound Alert")
            alert_level = "Low" # Setting alert level for a sound alert to low 
        
        if (gasDetected): # Gas
            alert_types.append("Hazardous Gas Alert")
            alert_level = "High" # Alert level for Gas is set to our highest alert level which is High
            activateFan = True
        
        
        if (alert_level == 'Low'):
            alert_list = str(alert_types)[1:(len(str(alert_types))-1)]
            email_alert(alert_list, recipient_email)
            low_alert() #if an alert is low, we call the low_alert function from Alerts.py
            
        elif (alert_level == 'High'):
            alert_list = str(alert_types)[1:(len(str(alert_types))-1)]
            email_alert(alert_list, recipient_email)
            high_alert() #if an alert is high, we call the high_alert function from Alerts.py
        
        if (activateFan):
            write2("FanOn") #writing using write2 function from Thingspeak.py
            time.sleep(5)
            write2("FanOff") #writing using write2 function from Thingspeak.py
            
        
        time.sleep(1) # wait 5 seconds
        
    

if __name__ == '__main__':
    dbconn = create_connection("")
    dataPolling(dbconn, "jackharold@cmail.carleton.ca") # sending the messages to the email address
    