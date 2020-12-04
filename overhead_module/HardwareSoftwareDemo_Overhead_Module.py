import urllib
import requests
import threading
import json
import time
from random import seed
from random import random
seed(1)
#importing libraries used further to be used in the codes

#    By Hovish Balgobin (Student ID: 101125942)
#    3rd Computer Systems Engineering Student
#    SYSC 3010 HardwareSoftwareDemo for the Overhead Module
#    Code+Testing




WriteKey='Z95PD6QGLPMMPF1V' #This is the key that will be used to write into a thingspeak channel
ReadActionKey='PXXBGX8G3UUZ8CXN' #This is the key that will be used to write into a thingspeak channel


#function getBabyTemperauter is simulating a thermal camera that can take readings of temperature at specific regions
def getBabyTemperature():
    #thermalcameraflag=False
    min = 35.0
    max = 39.9 #defining range
    
    temperature = min + (random()*(max-min)) #formula for random generator
    return temperature
        

#function MobileAction is used to set up the Mobile in action based on the parameter Action.
def MobileAction(Action):
    
    mobileflag=False #simulating the motion of the mobile
    
    if (Action == "Action"):
        
        mobileflag = True #true means the mobile is moving
        print("mobile is moving")
    
    elif(Action == "NoAction"):
        
        mobileflag = False #false means mobile is not moving
        print("........................")
    
    return mobileflag
  
POLLING_TIMEOUT = 3 #Used for a poling loop for the testing part



#function uploadDataOverhead is used to upload a specific temperature to a thinkspeak channel
def uploadDataOverhead(temperature): #writing to channel
    
    Write_URL = 'https://api.thingspeak.com/update?api_key=Z95PD6QGLPMMPF1V&field1=' #Writing URL
    
    f = urllib.request.urlopen(Write_URL + str(temperature))#requesting to be able to write
    f.read
    f.close     

#function is used to read an Action from a thinkspeak channel where data is being
#sent from a database
def ActionRead(): #Reading from channel
    
    URL = 'https://api.thingspeak.com/channels/1228612/fields/1.json?results=2' #Reading channel field
    
    get_data =requests.get(URL).json() #setting the data in a json format
    action=get_data['feeds'][0]['field1'] #getting the data from field1
    id_message= get_data['channel']['last_entry_id']   
    
    print(action)
    return [id_message,action]#this is used to return an array with both
                              #a time ID and the action asscoiated to it

#function testing is used to test the above system code.
def testing():
    
    starting_id = ActionRead()[0] #accessing the first element of the array being returned by ActionRead
    flagtemp= False
    flagaction=False #Initialisation of flags
    dummy_temperature=25
    
    # Dummy temperature is used to verify if the temperature is being uploaded
    uploadDataOverhead(dummy_temperature)
    
    URL_READ= 'https://api.thingspeak.com/channels/1161231/fields/1.json?results=2'
    #reading dummy variable
    
    get_data =requests.get(URL_READ).json()
    new_temp=get_data['feeds'][0]['field1']
    #attempting to acquire data from the thinkspeak channel
    
    
    if (int(new_temp) == dummy_temperature):
     #comparing the data transferred and reading back
        
        flagtemp= True
        print("The writing temperature channel is working properly") #Data matched
        
    else:
        
        print("The writing temperature is not working") #Data does not match

    print("---------------------------") #aesthetic
    
    response_data ="" #Variable used to find if action can be read
    
    i=0 #used for a polling loop
    
    while i <= POLLING_TIMEOUT: #polling loop used to ensure that data can be read
        
        read_data = ActionRead()
        if(read_data[0] > starting_id): #checking if a response has been received
            
            print("Response Received")
            response_data = str(read_data[1]) 
            #print(response_data)
            break; #out of the loop
        
        time.sleep(1) #Puts the system in sleep for 1 second
        i+=1 #increments i if not found
    
    if (response_data =="Action"): #verifying if matched
        
        print("Action succesfully read")
        flagaction = True #Used for final testing
        
    else:
        
        print("Action not read")
        flagaction= False #used for final condition
      
    testmobile = False
    
    if (MobileAction(response_data)):# Verifying response data
        
        print("Test for mobile is succesful")
        testmobile = True #Switching flag for final condition
        
    else:
        
        print ("Test Mobile failed")
        testmobile=False #Switching flag for final condition
    
##    TemperatureTestFlag=[False,False,False]
##    Temperature=[37.9,-12.3,38.0]
##    for i in Temperature: 
#used if code was trying to implement conditions
        
    TemperatureTestFlag=False #Switching flag for final condition
    Temp =getBabyTemperature() # Inputing returned value in Temp
    
    if ((Temp>=35.0)and (Temp<=39.9)): #condtion to check if Thermal Camera is working        
        
        TemperatureTestFlag = True  #Switching flag for final condition
        print("Temperature Sensor is working properly")
        
    else:
        
        TemperatureTestFlag = False #Switching flag for final condition
        print ("Temperature Sensor is not working")        

        

    if(flagtemp and flagaction and TemperatureTestFlag and testmobile):
        #Final statement passes if all flag return true, fails otherwise
        print("Test Succesful")
        
        
    else:
        
        print("Test Failed")
        

#Runs the entire testing function.
if __name__=='__main__': 
    testing()
    
    

    
