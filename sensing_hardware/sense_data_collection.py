from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def getRoomTemp(): #returns float RoomTemp
    return round(sense.get_temperature(), 1)

def getRoomHumidity(): #returns float RoomHumidity
    return round(sense.get_humidity(), 1)

def getCribMovement(): #returns float CribMovement
    acceleration = sense.get_accelerometer_raw()
    x = abs(acceleration['x'])
    y = abs(acceleration['y'])
    z = abs(acceleration['z'])
    average = round((x+y+z)/3, 3)
    return average

#continuously prints collected data
while True:
    print("Temp=%s, Humidity=%s, Acceleration=%s" % (getRoomTemp(), getRoomHumidity(), getCribMovement()))
    sleep(.5)
