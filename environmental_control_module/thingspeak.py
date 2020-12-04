import urllib
import requests
import threading
import json

# Modified From Lab 2 Thinkspeak Part 3

# URL List: [Id, Read Key, Write Key]
Sending_URL_List = ["1161308", "8XPC82KQHOMRB0V3", "K4ZAS7GQ7CV30OEZ"]
Recieving_URL_List = ["1228334", "U7JYW9E8QKOK1NHD", "JZTUTXH0X9KV5WV9"]

# Write to a channel
def _thingspeak_post(url_list, message, data):
    
    URl='https://api.thingspeak.com/update?api_key='
    KEY= url_list[2]
    HEADER='&field1={}&field2={}'.format(message,data)
    NEW_URL=URl+KEY+HEADER
    #print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    #print(data)

# Read from a channel (Internal Function)
def _read_data_thingspeak(url_list):
    URL='https://api.thingspeak.com/channels/' + url_list[0] + '/feeds.json?api_key='
    KEY= url_list[1]
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER
    #print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    
    try:
        last_entry_id=get_data['channel']['last_entry_id']
        Message=get_data['feeds'][0]['field1']
        Data=get_data['feeds'][0]['field2']
    except:
        return False
    
    return [last_entry_id, Message, Data]




# Write Message to Alert Channel
def action_write(alert_type):
    
    # Get existing state of channel
    existing_data = _read_data_thingspeak(Sending_URL_List)
    if (not existing_data): return False

    last_entry_id = int(existing_data[0])
    
    # Post to the channel
    _thingspeak_post(Sending_URL_List, "environmentAlert", alert_type)
    
    # Check that the channel has been updated
    new_data = _read_data_thingspeak(Sending_URL_List)
    if (not new_data): return False

    # Verify the updated data
    return ( (int(new_data[0]) == last_entry_id + 1) and (new_data[1] == "environmentAlert") and (new_data[2] == alert_type) )
    
# Read Latest Message from the Control Channel
def action_read():
    
    read_data = _read_data_thingspeak(Recieving_URL_List)
    if(not read_data): return False
    
    return read_data


# E2E_Test Testing Code
#if __name__ == '__main__':
#    _thingspeak_post(Recieving_URL_List, "controlFan", "FanOn")
#    time.sleep(5)
#    _thingspeak_post(Recieving_URL_List, "controlFan", "FanOff")
