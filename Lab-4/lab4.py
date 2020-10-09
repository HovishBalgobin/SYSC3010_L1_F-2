from urllib.parse import urlencode 
import time
import http.client as http
from urllib.request import urlopen

key = "7481QW0APO2BO2BU"
Project_Group= "L1-f-2"
Member_Identifier="a"
cmail_address="hovishbalgobin@cmail.carleton.ca"

URL='http://api.thingspeak.com/update?api_key='
HEADER='&field1={}&field2{}&field3{}'.format(Project_Group,Member_Identifier,cmail_address)
new_url=URL+key+HEADER
print(new_url)
update= urlopen(new_url)
print(update)





##baseURL1 = '
##baseURL2=  'http://api.thingspeak.com/update?api_key=7481QW0APO2BO2BU&field2='
##baseURL3=  'http://api.thingspeak.com/update?api_key=7481QW0APO2BO2BU&field3='
##print (Project_Group)
##f=urllib3.urlopen(baseURL1 + str(Project_Group))
##f.read
##f.close
##print (Member_Identifier)
##f=urllib3.urlopen(baseURL2 + str(Member_Identifier))
##f.read
##f.close
##print (cmail_address)
##f=urllib3.urlopen(baseURL3 + str(cmail_address))
##f.read
##f.close
##print("End")
##    
##                