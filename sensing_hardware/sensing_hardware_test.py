import http.client
import urllib.parse
from sense_hat import SenseHat
import time
import requests

sense = SenseHat()

def getRoomTemp(): #returns float RoomTemp
    return round(sense.get_temperature(), 1)

def getRoomHumidity(): #returns float RoomHumidity
    return round(sense.get_humidity(), 1)

def getCribMovement(): #returns float CribMovement
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    average = round(((x + y + z)/3), 2)
    return average

key = "L1OFSYJ2OUUAM7JT"

def uploadData(roomTemp, roomHumidity, cribMovement): #uploads the 3 data

    params = urllib.parse.urlencode({'field1': roomTemp, 'field2': roomHumidity, 'field3': cribMovement, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    # upload
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")


while True:
    roomT = getRoomTemp()
    roomH = getRoomHumidity()
    cribM = getCribMovement()
    uploadData(roomT, roomH, cribM)
    time.sleep(20)
