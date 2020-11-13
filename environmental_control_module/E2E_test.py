import thingspeak
import time
import datetime

# Response Polling timout in Seconds
POLLING_TIMEOUT = 30


def e2e_testsuite():
    
    # Determing Reference id to check for new incoming messages
    starting_id = thingspeak.action_read()[0]
    
    test_status = True
    
    print("---------------------------")
    print("Begin End-to-End Tests:")
    print("---------------------------")
    
    # Attempt to write an alert to the Alert Channel (L1_F_2b1)
    if (thingspeak.action_write("GasAlert")):
        print("Write GasAlert to 'Alert Channel': SUCCEEDED")
    else:
        print("Write GasAlert to 'Alert Channel': FAILED")
        test_status = False
    
    print("---------------------------")
    
    # Wait for a message in the Command Channel (L1_F_2b2)
    print("Begin Waiting for a Response Message on the 'Command Channel'...")
    
    # Begin polling the Command Channel until a new message is sent to the channel
    response_data = ""
    i = 0
    
    while i <= POLLING_TIMEOUT:
        read_data = thingspeak.action_read()
        if(read_data[0] > starting_id):
            print("Response Received")
            response_data = read_data[2]
            break;
        
        time.sleep(1)
        i += 1
    
    # Verify the correct message was sent
    if (response_data == "FanOn"):
        print("Fan Command from 'Command Channel': RECEIVED")
    else:
        print("Fan Command from 'Command Channel': FAILED")
        test_status = False
        
    print("---------------------------")
    print("End-to-End Test Status: " + ("PASSED" if test_status else "FAILED") )
    print("---------------------------")
    
    return test_status




if __name__ == '__main__':
    e2e_testsuite()
