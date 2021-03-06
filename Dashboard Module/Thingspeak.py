import http.client
import urllib
from urllib.request import *
import json
import requests
# all imports handled from line 1 - 5
write_key1 = "JZTUTXH0X9KV5WV9" # write key for one of the channels that messages will be written to
write_key4 = "8ANZIHT63EOH0M3Z" # write key for one of the channels that messages will be written to



def write1(on1): # a simple function to write to a channel
    while True:
        params = urllib.parse.urlencode({'field1': on1, 'key':write_key1 }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
def write2(on2): # fucntion to write to a second channel
    while True:
        params = urllib.parse.urlencode({'field1': on2, 'key':write_key4 }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def read1(number_of_results): #function to read a string message from this channel
    url = 'https://api.thingspeak.com/channels/1161308/feeds.json?api_key=8XPC82KQHOMRB0V3&results='
    url += str(number_of_results)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    results = [ str(current["field2"]) for current in subject ]
    return results

def read2(): #function to read Baby Temperature values from this channel
    url = 'https://api.thingspeak.com/channels/1161231/feeds.json?api_key=476KA0ACBHVN9DFY&results=1'
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    return current["field1"]

def read3(): # function to read Room Temperature, Room Humidity and Crib Movement 
    url = 'https://api.thingspeak.com/channels/1228565/feeds.json?api_key=TIQMWNUMC2X62HSF&results=1'
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    results = [current["field1"],current["field2"],current["field3"]]
    return results 
    
def get_entry_id(): # this function returns the entry id of a value
    url = 'https://api.thingspeak.com/channels/1161308/feeds.json?api_key=8XPC82KQHOMRB0V3&results=1'
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    return current["entry_id"]
    

    
    
    