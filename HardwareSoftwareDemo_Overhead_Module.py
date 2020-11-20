import urllib
import requests
import threading
import json
import time
from random import seed
from random import random
seed(1)
thermalcameraflag=False



WriteKey='Z95PD6QGLPMMPF1V'
ReadActionKey='PXXBGX8G3UUZ8CXN'



def getBabyTemperature():
    #thermalcameraflag=False
    min = 35.0
    max = 39.9
    temperature = min + (random()*(max-min))
    return temperature
        

def MobileAction(Action):
    mobileflag=False
    if (Action == "Action"):
        mobileflag = True
        print("mobile is moving")
    
    elif(Action == "NoAction"):
        mobileflag = False
        print("........................")
    
    return mobileflag
  
POLLING_TIMEOUT = 3




def uploadDataOverhead(temperature): #writing to channel
    Write_URL = 'https://api.thingspeak.com/update?api_key=Z95PD6QGLPMMPF1V&field1='
    f = urllib.request.urlopen(Write_URL + str(temperature))
    f.read
    f.close     
    
def ActionRead(): #Reading from channel
    URL = 'https://api.thingspeak.com/channels/1228612/fields/1.json?results=2' #Reading channel field
    get_data =requests.get(URL).json()
    action=get_data['feeds'][0]['field1']
    id_message= get_data['channel']['last_entry_id']   
    
    print(action)
    return [id_message,action]

def testing():
    starting_id = ActionRead()[0]
    flagtemp= False
    flagaction=False
    dummy_temperature=25
    uploadDataOverhead(dummy_temperature)
    URL_READ= 'https://api.thingspeak.com/channels/1161231/fields/1.json?results=2' #reading dummy variable
    get_data =requests.get(URL_READ).json()
    new_temp=get_data['feeds'][0]['field1']
    if (int(new_temp) == dummy_temperature):
        flagtemp= True
        print("The writing temperature channel is working properly")
    else:
        print("The writing temperature is not working")

    print("---------------------------")
    response_data =""
    i=0
    
    while i <= POLLING_TIMEOUT:
        read_data = ActionRead()
        if(read_data[0] > starting_id):
            print("Response Received")
            response_data = str(read_data[1])
            #print(response_data)
            break;
        time.sleep(1)
        i+=1
    
    if (response_data =="Action"):
        print("Action succesfully read")
        flagaction = True
        
    else:
        print("Action not read")
        flagaction= False
      
    testmobile = False
    if (MobileAction(response_data)):
        print("Test for mobile is succesful")
        testmobile = True
    else:
        print ("Test Mobile failed")
        testmobile=False 
    
    TemperatureTestFlag=[False,False,False]
    Temperature=[37.9,-12.3,38.0]
    for i in Temperature:
        
    TemperatureTestFlag=False
    Temp =getBabyTemperature()
    if ((Temp>=35.0)and (Temp<=39.9)):
        TemperatureTestFlag = True
        print("Temperature Sensor is working properly")
    else:
        TemperatureTestFlag = False
        print ("Temperature Sensor is not working")        

        

    if(flagtemp and flagaction and TemperatureTestFlag and testmobile):
        print("Test Succesful")
    else:
        print("Test Failed")
        

        

testing()

    

    
