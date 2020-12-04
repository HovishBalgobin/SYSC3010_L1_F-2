import tkinter as tk #importing the interface for the buuiliding of the GUI
from tkinter import *
import sqlite3 #Importing for interaction with the database
from Engine import *
from Database import *
#from email_notif import email_alert

editable_flag=True #flag being used to allow user to 
password_saved="" #global variables for GUI variables
password_try=""
Name=""

global email_entry_send
email_entry_send = ""

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
    
    dbconn = create_connection("")
    
    def create_button(window,name,command_passed): #function to create buttons
        button=tk.Button(window,text=name,command=command_passed)
        button.pack()
        
    def toggle_flag(): #function to toggle the flags for passwords, passwords are required if flag is false
        global editable_flag
        editable_flag= not(editable_flag)
        
        
    def register_window(): #window for the registration of parameters
##        print(toggle_flag())
        global password_saved
        global Name
        if(editable_flag):
            toggle_flag()        
        else:
            reset_window()           
       
        print(editable_flag)
        registerwindow = tk.Toplevel(window);
        registerwindow.geometry('400x400')
        
        name_label=tk.Label(registerwindow,text="Name of Baby")
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
        room_min_entry.pack()   
        
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
            Name = name_entry.get()
            
##            modify_parameters(room_min_entry.get(),room_max_entry.get(),roomH_min_entry.get(),roomH_max_entry.get())
            email_entry_send = email_entry.get()
            print(email_entry_send,"test",email_entry.get())
            
##            baby_max_entry.get()
##            baby_min_entry.get() 
            registerwindow.destroy()
        
        
        create_button(registerwindow,"SAVE",savedata) #save button used to save registered data
    
    def password_window(): #password window called whenever password is required to change parameters
        global password_try 
        passwordwindow = tk.Toplevel(window);
        passwordwindow.geometry('200x200')
        
        trypassword_label=tk.Label(passwordwindow,text="Enter Password")
        trypassword_entry=tk.Entry(passwordwindow)
        trypassword_label.pack()
        trypassword_entry.pack()
        
        def trying_password():
            password_try = trypassword_entry.get()
            
            print (password_try)
            passwordwindow.destroy()
        
        create_button(passwordwindow,"SAVE", trying_password)        
        
       
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
        register_window()
        
        
        
        
    def SmartCrib(recipient_email):
        print(email_entry_send,"test")
        dataPolling(dbconn,recipient_email)
                #function starting the whole process
                #The Smartcrib function is the function that is set in motion when we press on the button "START" on the main screen
                #This should trigger all of our codes and start the project
                #Alongside all data being recorded, actions being sent must start being displayed as soon as this function is called
              #To be completed
        informationcall= getLastDataEntries(dbconn,1)[0]
        textbox.insert(Insert,"The temperature of the room is :"+ informationcall[3]) #To be Completed
        textbox.insert(Insert,"The temperature of" + Name + "is :"+ informationcall[1]) # To be completed
        textbox.insert(Insert,"The humidity of the room is :"+ informationcall[4]) #TO be completed
        ##textbox.insert(Insert,"The gas concentration of the room is :"+ getLastDataEntries(dbconn,1)[3])
        
    def Stop():
        stopPolling()
                #function stopping the process
                #function to be completed
        
    create_button(window,"START",lambda : SmartCrib(email_entry_send))
    #button= Tk.Button(master=window,text="START",command= lambda : SmartCrib(email_entry_send)) #Uncomment Later
    #button.pack()
        
    create_button(window,"REGISTER",register_window)
##    create_button(window."EDIT",edit_window)
    create_button(window,"RESET",reset_window)
    
    create_button(window,"STOP",Stop) #Uncomment Later
    
    textbox= Text(window,height=20,width=40) 
    textbox.pack()
    
    
    
    
    
        

if __name__ == "__main__":
    create_welcome_window()

    #register_window()

