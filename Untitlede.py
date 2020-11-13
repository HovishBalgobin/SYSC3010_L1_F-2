import json
import requests
import urllib.request


# Channel: [Id, Read Key, Write Key]

Channel_1 = ["JZTUTXH0X9KV5WV9"] # writing from this channel
Channel_2 = ["1161308", "8XPC82KQHOMRB0V3"] # reading from this channel
Channel_3 = ["1161231", "476KA0ACBHVN9DFY"] # reading from here
Channel_4 = ["8ANZIHT63EOH0M3Z"] # writing from here
Channel_5 = ["1228565","TIQMWNUMC2X62HSF"] # reading from here

on1 = "MobileOn"
on2 = "FanOn"
off1 = "MobileOff"
off2 = "FanOff"

def read(key,Id):
    URL = 'https://api.thingspeak.com/channels/'+Id+'/feeds.json?api_key='
    HEADER = '&result=0'
    nURL = URL+key+HEADER
    #print (nURL)
    getData = requests.get(nURL).json()
    #print (getData)
    channeId = getData['channel']['id']
    feed1 = getData['feeds']
    
     
    if (Id == "1161231"):
        code = 0
        for x in feed1:
            code = x['field1']
        print("Baby Temperature is {}.".format(code))
    
    if (Id == "1228565"):
        code1 = 0
        code2 = 0
        code3 = 0
        for x in feed1:
            code1 = x['field1']
            code2 = x['field2']
            code3 = x['field3']
        print("Temperature is {}, Humidity is {}, Movemement is {}".format(code1,code2,code3))
       
    if (Id == "1161308"):
        code1 = ''
        code2 = 0
        for x in feed1:
            code1 = x['field1']
            code2 = x['field2']
        print("Gas Alert")
    
def write(key,ms1):
 
    URL = 'https://api.thingspeak.com/update?api_key='
    HEADER = '&field1={}'.format(ms1)
    NEWURL = URL+key+HEADER
    print(NEWURL)

    data = urllib.request.urlopen(NEWURL)
    print(data)
    print("The message written is " + ms1) 
    
if __name__ == '__main__':
    write("JZTUTXH0X9KV5WV9",on1)
    write("8ANZIHT63EOH0M3Z",on2)
    
    