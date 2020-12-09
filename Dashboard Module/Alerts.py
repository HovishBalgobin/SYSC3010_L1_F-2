import RPi.GPIO as GPIO # import
import time
GPIO.setmode(GPIO.BOARD) # choose Board

GPIO.setup(7, GPIO.OUT) # set GPIO7 as an output
GPIO.setup(11, GPIO.OUT) # set GPIO11 as an output


def low_alert():  # This function will turn on only one of the LED lights on the breadboard  
    GPIO.output(7, True) # setting the port/pin value to True/GPIO.HIGH
    time.sleep(5) # wait 5 seconds
    GPIO.output(7, False) # setting the port/pin value to False/GPIO.LOW
    
    
    
def high_alert(): # This function will turn on both of the LED Lights to show that there is a major issue occuring
    GPIO.output(7, True) # setting the port/pin value to True/GPIO.HIGH
    GPIO.output(11, True) # setting the port/pin value to True/GPIO.HIGH
    time.sleep(5) # wait 5 seconds
    GPIO.output(7, False) # setting the port/pin value to False/GPIO.LOW
    GPIO.output(11, False) # setting the port/pin value to False/GPIO.LOW
        