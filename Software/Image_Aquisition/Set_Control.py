# Developed by Logan Rower
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
## Today's Date
today_date = datetime.today().strftime("%Y%m%d")
## Current Time in HH:MM:SS
current_time = datetime.now()
print("Current Time:", current_time.strftime("%H%M%S"))
## time from now for when you want to start
print("Input number of hours, minutes and seconds from current time to start experiment")
hr_input = int(input("Hours:"))
min_input = int(input("Minutes:"))
sec_input = int(input("Seconds:"))
tdelta = timedelta(seconds = sec_input, minutes = min_input, hours = hr_input)
## now define the start time of the experiment  
exp_start = (current_time + tdelta).strftime("%Y%m%d%H%M%S")

# Duration of the Experiment:
duration_hr = int(input("Duration of Experiment (hr):"))
duration_min = int(input("Duration of Experiment (min):"))
duration_sec = int(input("Duration of Experiment (sec):"))
dur_delta = [duration_hr,duration_min, duration_sec]
## Will use time delta in the main script1
#duration_delta = timedelta(seconds = duration_sec, minutes = duration_min, hours = duration_hr)
#prin
# Frame Rate
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
