import urllib
import requests
import threading
import json
import time



WriteKey='Z95PD6QGLPMMPF1V'
ReadActionKey='PXXBGX8G3UUZ8CXN'

##def getBabyTemperature()
##def MobileAction(Action)


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
    print(action)
    return action

def testing():
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
    starting_id = ActionRead()[0]
    while i <= POLLING_TIMEOUT:
        read_data = ActionRead()
        if(read_data[0] > starting_id):
            print("Response Received")
            response_data = str(read_data[2])
            break;
        time.sleep(1)
        i+=1
    if (response_data == str("Action")):
        print("Action succesfully read")
        flagaction = True
        
    else:
        print("Action not read")
        

    if(flagtemp and flagaction):
        print("Test Succesful")
    else:
        print("Test Failed")
        

        

testing()

    

    
