from sense_hat import SenseHat
from time import sleep
counter =0


sense = SenseHat()
## creating a variable to make use of the SenseHat in-built functions
sense.clear()
## clearing the display

purple = (148,0,211)
##creating purple using the RGB values

def show_H():
  sense.show_letter("H",back_colour= purple)
  #time.sleep(.5)
  
##function to display H whenever it is called with a purple background.
  
def show_B():
  sense.show_letter("B", back_colour = purple)
  #time.sleep(.5)
  
##function to display B whenever it is called with a purple background.

def repeat(flag):
    if (flag==True):
        show_H()
        
       
    elif(flag==False):
        show_B()
        #flag = True
        
    flag=not(flag)
    return flag

## function used to display the letters and toggle the flag.

    
selection = False    #initialising selection and Flag    
Flag= True;
while True: 
  
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":        
         Flag = repeat(Flag)
         if (sense.stick.get_events()==UP):
             counter++
         if  (sense.stick.get_events()==DOWN):
            counter--
        
         selection = True
         
sense.clear()










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