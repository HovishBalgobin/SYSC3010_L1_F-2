# SYSC 3010 - Smart Crib Design

## Authors:
- Hovish Balgobin
- Jack Harold
- Mehdi Khan
- Oluwaseyi Sehinde-Ibini

## How to run each Module on a Raspberry Pi 4

### Dashboard
- Start by connecting the hardware with:
  - the major alarm lights attached to GPIO port 4
  - the minor alarm lights attached to GPIO port 17 
- Run `python3 Engine.py` from the "Dashboard Module" folder

### Environment Control
- Start by connecting the hardware with:
  - the gas sensor input attached to GPIO port 11
  - the sound sensor attached to GPIO port 29
  - the fan switch attached to GPIO port 31 
- Run `python3 sensing.py` from the environmental_control_module folder

### Overhead Module
- No hardware setup necessary (All Hardware for this unit is )
- Run `python3 Final_Demo_Overhead_Module.py` from the overhead_module folder


### Sensing Module
- Start by attaching the senseHat to the Pi
- Run `python3 .sensing.py` from the sensing_module folder


## Git File Structure

├── Dashboard Module (Central Communication Node with GUI)
    ├── Alerts.py
    ├── Database.py
    ├── email_notif.py
    ├── Engine.py
    ├── GUI_Structure.py
    ├── projectdatabase.db
    ├── Thingspeak.py
    └── Untitlede.py
 
├── environmental_control_module (Hazard detection module with gas, sound sensors and fan)
    ├── E2E_test.py
    ├── environment_control_module.py
    ├── HW_test.py
    ├── peripheralInterfaces.py
    └── thingspeak.py
 
├── Lab-5 (3010 Lab 5 - Not a part of the final crib design)
    ├── AB.py
    ├── A.py
    ├── B.py
    ├── CD.py
    ├── C.py
    ├── D.py
    └── Lab5.py
 
├── overhead_module (Overhead mounted module with thermal camera and mobile)
    ├── end-to-end-demo.py
    ├── Final_Demo_Overhead_Module.py
    └── HardwareSoftwareDemo_Overhead_Module.py
 
├── README.md (You are Here!)
 
├── sensing_hardware 
    ├── sense_data_collection.py
    └── sensing_hardware_test.py
└── sensing_module (Atmospheric Sensing Platform with senseHat)
    ├── E2E_fixed_test.py
    ├── E2E_sense_test.py
    └── sensing.py






