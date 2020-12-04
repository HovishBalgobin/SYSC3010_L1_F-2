import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


def low_alert():
    
    GPIO.output(7, True)
    time.sleep(5)
    GPIO.output(7, False)
    
    
    
def high_alert():
    GPIO.output(7, True)
    GPIO.output(11, True)
    time.sleep(5)
    GPIO.output(7, False)
    GPIO.output(11, False)
        