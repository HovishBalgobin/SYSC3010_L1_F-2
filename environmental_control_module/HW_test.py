import peripheralInterfaces
import time
import datetime

# Response Polling timout in Seconds
POLLING_TIMEOUT = 30


def hw_testsuite():
    
    peripheralInterfaces.initializePeripherals()
    
    test_status = True
    
    print("---------------------------")
    print("Begin Hardware Tests:")
    print("---------------------------")
    
    
    print("Begin Waiting for Alerts from the Gas Sensor and Sound Sensor...")
    
    # Initialize the polling flags
    gasDetected = False
    soundDetected = False
    
    i = 0
    
    # Begin Polling for Alerts 
    while i <= POLLING_TIMEOUT:
        newEvents = peripheralInterfaces.wasSensorTriggered()
        if (not gasDetected and 'GasAlert' in newEvents):
            print("Gas Alert Detected!")
            gasDetected = True
        if (not soundDetected and 'SoundAlert' in newEvents):
            print("Sound Alert Detected!")
            soundDetected = True
            
        if (gasDetected and soundDetected): break;
        
        time.sleep(1)
        i += 1
    
    if (gasDetected and soundDetected):
        print("Receive Alert from Gas Sensor and Sound Sensor: SUCCEEDED")
    else:
        print("Receive Alert from Gas Sensor and Sound Sensor: FAILED")
        test_status = False
    
    print("---------------------------")
    
    
    # Turn on the Fan for 5 seconds and then turn it off again
    print("Begin Fan Control Test for 5 seconds...")
    
    peripheralInterfaces.controlFan(True)
    time.sleep(5)
    peripheralInterfaces.controlFan(False)
    
    print("End Fan Control Test")
    
        
    print("---------------------------")
    print("Hardware Test Status: " + ("PASSED" if test_status else "FAILED") )
    print("---------------------------")
    
    peripheralInterfaces.closePeripheralGPIO()
    
    return test_status




if __name__ == '__main__':
    hw_testsuite()

