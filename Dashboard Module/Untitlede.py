import json
import requests
import urllib.request
import time


# Channel: [Id, Read Key, Write Key]

Channel_1 = ["JZTUTXH0X9KV5WV9"] # writing from this channel
Channel_2 = ["1161308", "8XPC82KQHOMRB0V3"] # reading from this channel Jack
Channel_3 = ["1161231", "476KA0ACBHVN9DFY"] # reading from here Hovish
Channel_4 = ["8ANZIHT63EOH0M3Z"] # writing from here
Channel_5 = ["1228565","TIQMWNUMC2X62HSF"] # reading from here Medi

on1 = "Action"
on2 = "FanOn"

POLLING_TIMEOUT = 30

def read(key,Id, fields):
    URL = 'https://api.thingspeak.com/channels/'+Id+'/feeds.json?api_key='
    HEADER = '&results=1'
    nURL = URL+key+HEADER
    #print (nURL)
    get_data = requests.get(nURL).json()
    #print (getData)
    
    try:
        last_entry_id=get_data['channel']['last_entry_id']
        if (fields >= 1):
            field_1=get_data['feeds'][0]['field1']
        else: field_1=""
        if (fields >= 2):
            field_2=get_data['feeds'][0]['field2']
        else: field_2=""
        if (fields >= 3):
            field_3=get_data['feeds'][0]['field3']
        else: field_3=""
    except:
        return False
    #print([Id, last_entry_id, field_1, field_2, field_3])
    return [last_entry_id, field_1, field_2, field_3]
    
     
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
    
def write(key,ms1,ms2,fields):
 
    URL = 'https://api.thingspeak.com/update?api_key='
    HEADER = '&field1={}'.format(ms1)
    if (fields >=2): HEADER += '&field2={}'.format(ms2)
    NEWURL = URL+key+HEADER
    #print(NEWURL)

    data = urllib.request.urlopen(NEWURL)
    #print(data)
    print("The message written is " + ms1) 
    
if __name__ == '__main__':
    
    old_value_1 = read(Channel_2[1], Channel_2[0], 2)
    old_value_2 = read(Channel_3[1], Channel_3[0], 1)
    old_value_3 = read(Channel_5[1], Channel_5[0], 3)
    response_data = ""
    i = 0
    
    # Jack
    while i <= POLLING_TIMEOUT:
        read_data = read(Channel_2[1], Channel_2[0], 2)
        if(read_data[0] > old_value_1[0]):
            print("Response Received")
            response_data = str(read_data[2])
            break;
        
        time.sleep(1)
        i += 1
    
    print(response_data)
    if(response_data == "GasAlert"):
        print("Pass")
    else:
        print("Fail")
        
    write("JZTUTXH0X9KV5WV9", "fanControl", on2, 2)
    
    response_data = ""
    i = 0
    
    # Hovish
    while i <= POLLING_TIMEOUT:
        read_data = read(Channel_3[1], Channel_3[0], 1)
        if(read_data[0] > old_value_2[0]):
            print("Response Received")
            response_data = read_data[1]
            break;
        
        time.sleep(1)
        i += 1
    
    if(response_data == "25"):
        print("Pass")
    else:
        print("Fail")
    
    write("8ANZIHT63EOH0M3Z", on1, "", 1)
    
    response_data = ""
    i = 0
    
    
    # Mehdi
    while i <= POLLING_TIMEOUT:
        read_data = read(Channel_5[1], Channel_5[0], 3)
        if(read_data[0] > old_value_3[0]):
            print("Response Received")
            response_data = read_data[1:4]
            break;
        
        time.sleep(1)
        i += 1
    if(response_data and str(response_data[0]) == "23.4" and str(response_data[1]) == "34.5" and str(response_data[2]) == "1.23"):
        print("Pass")
    else:
        print("Fail")
    
    
    
    