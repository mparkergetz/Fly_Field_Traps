# Developed by Logan Rower
# 7/6/2022 newest version..
from datetime import datetime, timedelta
import json
"""
This python script is to be run on the ubuntu machine that will be acting as the main server.
In order to appropriately sync the pies so that they are all communicating at the same time the user needs to run this script
before starting the experiment. This will allow for the following parameters to be changed after this control file is sent to all the 
pi devices.

dictionary to json...

PARAMETERS:
- start time
- duration of experiment
- frame rate
(brightness, contrast...) -> more to be and can be added for greater control
"""
# Start Time
## Current Time in HH:MM:SS
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
current_time = datetime.strptime(current_time,"%Y%m%d%H%M%S")
print("Current Time:", current_time)
## time from now for when you want to start
print("Time to Start Experiment")
start_input=input("HH:MM:SS ")
start_int = start_input.split(":")
exp_start=current_time.replace(hour = int(start_int[0]), minute = int(start_int[1]), second = int(start_int[2]))
print("Start Time:", exp_start)
## now define the start time of the experiment  
exp_start = exp_start.strftime("%Y%m%d%H%M%S")

# Duration of the Experiment:
print("Input Duration of Experiment")
dur_input = input("HH:MM:SS ")
duration = dur_input.split(":")
dur_delta = [int(duration[0]),int(duration[1]), int(duration[2])]
dur2_delta = timedelta(seconds =int(duration[2]), minutes = int(duration[1]), hours = int(duration[0]))

# End Time:
end_time = (datetime.strptime(exp_start,"%Y%m%d%H%M%S")+dur2_delta)
print("End Time:", end_time)

# Frame Rate
## Add this in!
frame_rate = 1 #fps

# control file parameters
control ={
    "start_time": exp_start,
    "duration": dur_delta,
    "frame_rate": frame_rate
}

# convert the file into json
with open("control.json", "w") as outfile:
    json.dump(control, outfile)
