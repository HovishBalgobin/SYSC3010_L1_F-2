import RPi.GPIO as GPIO
from queue import Queue

# Peripheral GPIO Channel Numbers
gasAlertChannel = 11
soundAlertChannel = 29
fanControlChannel = 31

# Begin the shared Queue for tracking events between threads
eventQueue = Queue()

# Callback functions to add each type of event to the eventQueue
def addGasAlert(channel):
    eventQueue.put(['GasAlert'])

def addSoundAlert(channel):
    eventQueue.put(['SoundAlert'])

# Set the GPIO config for the sensors. Run this before any other function
def initializePeripherals():
    # Setup the GPIO channels
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gasAlertChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(soundAlertChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(fanControlChannel, GPIO.OUT)
    
    # Link the callback functions to their GPIO channels
    GPIO.add_event_detect(gasAlertChannel, GPIO.FALLING, callback=addGasAlert)
    GPIO.add_event_detect(soundAlertChannel, GPIO.FALLING, callback=addSoundAlert)


# Clean up the GPIO config of the sensors. RUn this after the seonsors are no longer needed
def closePeripheralGPIO():
    GPIO.cleanup([gasAlertChannel, soundAlertChannel, fanControlChannel])

# Set the fan's state depending on the input
def controlFan(state):
    GPIO.output(fanControlChannel, state)

# Return all the events currently in the eventQueue and remove them from the queue
def wasSensorTriggered():
    events = []
    
    while not eventQueue.empty(): events += eventQueue.get()
    
    return events

