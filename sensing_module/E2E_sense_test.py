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


def readLast(): #reads last send data
    URL = 'https://api.thingspeak.com/channels/1228565/feeds.json?api_key=TIQMWNUMC2X62HSF&results=1'
    get_data = requests.get(URL).json()
    field = get_data['feeds']
    data = []
    for x in field:
        data.append(float(x['field1']))
        data.append(float(x['field2']))
        data.append(float(x['field3']))
    return data


def comparison(array1, array2): #comepares sent data to recieved data
    if array1 == array2:
        print("PASS")
    else:
        print("FAIL")


roomT = getRoomTemp()
roomH = getRoomHumidity()
cribM = getCribMovement()
dataCriteria = [roomT, roomH, cribM]

uploadData(roomT, roomH, cribM)
print("Data sent")
time.sleep(2)
readData = readLast()

comparison(dataCriteria, readData)
