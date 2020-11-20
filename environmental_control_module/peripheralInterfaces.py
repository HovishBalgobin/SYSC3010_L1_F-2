import RPi.GPIO as GPIO
from queue import Queue
from threading import Thread


gasAlertChannel = 11
soundAlertChannel = 29
fanControlChannel = 31

eventQueue = Queue()

soundAlreadyDetected = False

def addGasAlert(channel):
    eventQueue.put(['GasAlert'])


def addSoundAlert(channel):
    eventQueue.put(['SoundAlert'])


def initializePeripherals():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gasAlertChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(soundAlertChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(fanControlChannel, GPIO.OUT)
    
    GPIO.add_event_detect(gasAlertChannel, GPIO.FALLING, callback=addGasAlert)
    GPIO.add_event_detect(soundAlertChannel, GPIO.FALLING, callback=addSoundAlert)



def closePeripheralGPIO():
    GPIO.cleanup([gasAlertChannel, soundAlertChannel, fanControlChannel])


def controlFan(state):
    GPIO.output(fanControlChannel, state)


def wasSensorTriggered():
    events = []
    
    while not eventQueue.empty(): events += eventQueue.get()
    
    return events

