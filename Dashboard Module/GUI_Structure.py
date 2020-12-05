import tkinter as tk #importing the interface for the buuiliding of the GUI
from tkinter import *
import sqlite3 #Importing for interaction with the database
from Engine import * 
from Database import * 

#from email_notif import email_alert


#    By Hovish Balgobin (Student ID: 101125942)
#    3rd Computer Systems Engineering Student
#    SYSC 3010 GUI Demo
#    This GUI was made for the Smart Crib Project and allows the user to interact with the system while setting
#    their own defined parameters. Preset parameters exists if the user does not want to input their desired
#    values.

editable_flag=True #flag being used to allow user to 
password_saved="" #global variables for GUI variables
password_try="" #global variable to store password being tried
Name="" #global variable used for communication with the database

global email_entry_send
email_entry_send = "" #initialising global variable to allow user to input data to the GUI

##dbconn = create_connection(r"pythonsqlite.db")

def create_welcome_window(): #Creating the main window for the interactions
    
    window = tk.Tk();
    window.geometry('704x528+100+100') #setting the size of the window 
    welcomelabel= tk.Label(
        text = "SMART CRIB WELCOME INTERFACE", #caption
        fg = "red",
        bg= "white"   
        )
    welcome = welcomelabel
    welcome.pack()
    
    dbconn = create_connection("") #Establishing connection with the database
    
    def create_button(window,name,command_passed): #function to create buttons
        button=tk.Button(window,text=name,command=command_passed)
        button.pack()
        
    def toggle_flag(): #function to toggle the flags for passwords, passwords are required if flag is false
        global editable_flag
        editable_flag= not(editable_flag)
        
        
    def register_window(): #window crreating function for the registration of parameters
##        print(toggle_flag())
        global password_saved #global variable used to store predefined password
        global Name
        if(editable_flag):
            toggle_flag()        
        else:
            reset_window()           
       
        print(editable_flag) #printing flag on window for verification
        registerwindow = tk.Toplevel(window);
        registerwindow.geometry('400x400') #setting the size of the register window
        
        name_label=tk.Label(registerwindow,text="Name of Baby") #creating labels and entry boxes for user to input data
        name_entry=tk.Entry(registerwindow)
        name_label.pack()
        name_entry.pack()
        
        email_label=tk.Label(registerwindow,text="Email of Responsible Party")
        email_entry=tk.Entry(registerwindow)
        email_label.pack()
        email_entry.pack() #creating the tetboxes for the user defined parameters
        
        
        room_max_label=tk.Label(registerwindow,text="Room Maximum Temperature")
        room_max_entry=tk.Entry(registerwindow)
        room_max_label.pack()
        room_max_entry.pack()
        
        room_min_label=tk.Label(registerwindow,text="Room Minimum Temperature")
        room_min_entry=tk.Entry(registerwindow)
        room_min_label.pack()
        room_min_entry.pack()   #Allowing user to input parameters to be compared
        
##        baby_max_label=tk.Label(registerwindow,text="Baby Maximum Temperature")
##        baby_max_entry=tk.Entry(registerwindow)
##        baby_max_label.pack()
##        baby_max_entry.pack()
##        
##        baby_min_label=tk.Label(registerwindow,text="Baby Minimum Temperature")
##        baby_min_entry=tk.Entry(registerwindow)
##        baby_min_label.pack()
##        baby_min_entry.pack()        
        
        roomH_max_label=tk.Label(registerwindow,text="Room Maximum Humidity")
        roomH_max_entry=tk.Entry(registerwindow)
        roomH_max_label.pack()
        roomH_max_entry.pack()        
        
        roomH_min_label=tk.Label(registerwindow,text="Room Minimum Humidity")
        roomH_min_entry=tk.Entry(registerwindow)
        roomH_min_label.pack()
        roomH_min_entry.pack()        
        
        password_label=tk.Label(registerwindow,text="Password")
        password_entry=tk.Entry(registerwindow)
        password_label.pack()
        password_entry.pack() #creating the tetboxes for the user defined parameters
        
        def savedata(): #function used to send data saved to the database
            password_saved = password_entry.get() #To be completed
            print(password_saved)            
            Name = name_entry.get() #Setting value inside global variable
            
##            modify_parameters(room_min_entry.get(),room_max_entry.get(),roomH_min_entry.get(),roomH_max_entry.get())
            email_entry_send = email_entry.get() #setting global variable with data input by user
            print(email_entry_send,"test",email_entry.get())
            
##            baby_max_entry.get()
##            baby_min_entry.get() 
            registerwindow.destroy() #destroying window after saving
        
        
        create_button(registerwindow,"SAVE",savedata) #save button used to save registered data
                                                      
    #function below is used to create a window whenever a password is needed for the modification of parameters.
    def password_window(): #password window called whenever password is required to change parameters
        global password_try 
        passwordwindow = tk.Toplevel(window);
        passwordwindow.geometry('200x200') #setting size of the window
        
        trypassword_label=tk.Label(passwordwindow,text="Enter Password")
        trypassword_entry=tk.Entry(passwordwindow)
        trypassword_label.pack()
        trypassword_entry.pack() #creating textbox and label for user to input password
        
        #function used as command whenever save is clicked in the passwordwindow 
        def trying_password(): #setting value of the password in the global variable for external access
            password_try = trypassword_entry.get()
            
            print (password_try)
            passwordwindow.destroy()
        
        create_button(passwordwindow,"SAVE", trying_password)  #creating save button in the password window      
        
    #function used to reset parameters of the system 
    def reset_window(): #reset window is used to clear every parameters and input new ones
        global password_saved
        global editable_flag
##        if (editable_flag==false):
        while (editable_flag==False):
            password_window()
            
            if(password_try != password_saved):
                password_window() 
            else:
                toggle_flag()
                print(editable_flag) ##bug
        register_window() #calling register window if password is correct
        
        
        
        
    def SmartCrib(recipient_email):
        print(email_entry_send,"test")
        dataPolling(dbconn,recipient_email)
                #function starting the whole process
                #The Smartcrib function is the function that is set in motion when we press on the button "START" on the main screen
                #This should trigger all of our codes and start the project
                #Alongside all data being recorded, actions being sent must start being displayed as soon as this function is called
              
        informationcall= getLastDataEntries(dbconn,1)[0] #connects with the database and provides us with an array of parameters
        textbox.insert(Insert,"The temperature of the room is :"+ informationcall[3]) #codes to add datat in the textbox
        textbox.insert(Insert,"The temperature of" + Name + "is :"+ informationcall[1]) 
        textbox.insert(Insert,"The humidity of the room is :"+ informationcall[4]) 
        ##textbox.insert(Insert,"The gas concentration of the room is :"+ getLastDataEntries(dbconn,1)[3])
        
    def Stop():
        stopPolling()
                #function stopping the process being triggered
        
    create_button(window,"START",lambda : SmartCrib(email_entry_send)) #using lambda function to prevent single thread issue
    #button= Tk.Button(master=window,text="START",command= lambda : SmartCrib(email_entry_send)) #Uncomment Later
    #button.pack()
        
    create_button(window,"REGISTER",register_window) #creating buttons on the main window for interaction
##    create_button(window."EDIT",edit_window)
    create_button(window,"RESET",reset_window)
    
    create_button(window,"STOP",Stop) #Uncomment Later
    
    textbox= Text(window,height=20,width=40)  #creating textbox for display of information
    textbox.pack()
    
    
    
    
    
        

if __name__ == "__main__": #running the GUI
    create_welcome_window()

    #register_window()

