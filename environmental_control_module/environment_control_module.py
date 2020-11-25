import peripheralInterfaces
import thingspeak
import time
from threading import Thread



def fanThread():
    # Determing Reference id to check for new incoming messages
    starting_id = thingspeak.action_read()[0]
    
    # Begin polling the Command Channel until a new message is sent to the channel
    response_data = ""
    
    while True:
        read_data = thingspeak.action_read()
        
        if(read_data[0] > starting_id):
            print("Response Received")
            response_data = read_data[2]
            
            if (response_data == "FanOn"):
                peripheralInterfaces.controlFan(True)
            elif (response_data == "FanOff"):
                peripheralInterfaces.controlFan(False)
            
        # Wait for 1 second between polling cycles
        # and exit if terminateThreads is set
        time.sleep(1)
        if (terminateThreads):
            print("Stopping fanThread...")
            return


def sensorThread():
    # Begin Polling for Gas/Sound Alerts 
    while True:
        newEvents = peripheralInterfaces.wasSensorTriggered()
        
        # For each type of alert, send a request
        if ('GasAlert' in newEvents):
            thingspeak.action_write("GasAlert")
            print("Gas Alert Detected!")
            
        if ('SoundAlert' in newEvents):
            thingspeak.action_write("SoundAlert")
            print("Sound Alert Detected!")
            
        # Wait for 1 second between polling cycles
        # and exit if terminateThreads is set
        time.sleep(1)
        if (terminateThreads):
            print("Stopping sensorThread..")
            return


def main():
    
    # Initialize GPIO and Threads
    peripheralInterfaces.initializePeripherals()
    
    try:
        global terminateThreads
        terminateThreads = False 
        
        fanExecution = Thread(target=fanThread, args=())
        sensorExecution = Thread(target=sensorThread, args=())
        
        # Start Threads
        fanExecution.start()
        sensorExecution.start()
        
        
        userInput = ""
        
        print("Environment Control Module is Running")
        print("Enter 'exit' to stop the program")
        while userInput != "exit":
                userInput = str(input())
            
            
        print("Environment Control Module Shutting Down...")
        terminateThreads = True
        peripheralInterfaces.closePeripheralGPIO()
        
    # Catch Keyboard Interrupts or other errors and clean the GPIO state properly
    except Exception as error:
        print(error)
        terminateThreads = True
        peripheralInterfaces.closePeripheralGPIO()
    


if __name__ == '__main__':
    main()


