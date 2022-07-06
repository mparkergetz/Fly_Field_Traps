# Developed by Logan Rower
# Field Trap Script
# Use the Flags to allow the user to run a different version of the script
"""
Flags:

'-t' -> Shows and saves a test image 

'-r' -> Runs the timelapse based on json parameters

This is the initial implementation with ZERO SOCKET 
"""
# from picamera import PiCamera
from picam_noir import PiCamera2
#import picam
from time import sleep, perf_counter
from datetime import datetime, timedelta
import os
import sys
import json
## have this script be something that is user friendly... let's try to convert this to a class later on...
## so then this can be later utilized as a function and imported to make things easier

# called PiCamera
camera = PiCamera2()
# hue fixx
camera.awb_mode = 'greyworld'
## FOR THE PIBEECAM
# camera.rotation = 270

# load the json file in
with open('control.json') as json_file:
    control_data = json.load(json_file)
start_time = control_data['start_time']
duration = control_data['duration']
frame_rate = control_data['frame_rate']

while True: 
    # follow the below model for an if statement
    # first if statement for getting a test image
    if sys.argv[1] == "-t":
        try:
            # the path for saving the folders to for the still images
            path = "/home/pi/Desktop/images/windtunnel_images/Still_Images/"
            camera.resolution = (2592, 1944)
            # Take 1 image to view for 30 seconds and can change this within the JSON FILE
            delay_time = 10
            # now for taking the 1 number of image with 30 second delay 
            # then introduce the file path and include the data and time into this as well..
            time_folder = str(datetime.now().strftime("%Y-%m-%d"))
            ## New path was created to save the images to
            path_new = os.path.join(path,time_folder)
            os.makedirs(path_new, exist_ok = True)
            # location where file will be saved was updated.
            location = path_new + "/%s.jpg"
            # Current time for the file
            time_current = datetime.now().strftime("%Y%m%d%_H%M%S.%f")
            # filename was generated
            filename = location % time_current
            # preview the images...
            camera.start_preview()
        
            # Image was saved to file location
            camera.capture(filename)
                    
            sleep(delay_time)
            # end the preview
            camera.stop_preview()
        except KeyboardInterrupt:
            print("Interrupt")
            break
  #   #   #   #   #   #   #   #   #   #   #   
# second condition is if user desires to run a timelapse
###  While within in input 2 there will be no camera preview.
    # run
    elif sys.argv[1] == "-r":
        run = True
        try:
            # path to save the images to the timelapse folder
            path = "/home/pi/Desktop/images/windtunnel_images/Timelapse/"
            camera.resolution = (2592, 1944)
            # set the frame rate (SET IN JSON)
            camera.framerate = frame_rate
            # set the duration (SET IN JSON)
            time_hr = duration[0]
            time_min = duration[1]
            time_sec = duration[2]
            #print("2")
            # developed the change in time:
            tdelta = timedelta(seconds = time_sec, minutes = time_min, hours = time_hr)
            # set the start time
            current_time = datetime.now().strftime("%Y%m%d%H%M%S")
            if current_time == start_time:
                # set the folder for the timelapse
                timelapse_folder = str(start_time)
                path_new = os.path.join(path,timelapse_folder)
                os.makedirs(path_new, exist_ok = True)
                # added the the time delta to the before time to get the ending time
                time_end = (datetime.strptime(start_time,"%Y%m%d%H%M%S") + tdelta)
                print(time_end.strftime("%Y%m%d%H%M%S"))
                ## checking how many images were created...
                #### comment this out when program is successful
                count = 1
                # documented the location for where all of the files will be saved
                ## now in the while loop the images will be added to this path
                location = path_new + "/%s.jpg"
                # now before timelapse starts name it based on
                print("starting the while loop")
                # started a preview so that the user can be able to see the image
                #camera.start_preview()
                start =  perf_counter()
                while datetime.now() <= time_end:
                    # new filename with current time
                    #time_current = datetime.now().strftime("%H:%M:%S")
                    time_current = datetime.now()
                    time_current_split = str(time_current.strftime("%H%M%S"))
                    filename = location % time_current_split
                    # saved the image
                    ## set the video port to true in order to enable fast image processing...
                    camera.capture(filename, use_video_port = True)
                    #camera.capture(filename)
                    
                    count +=1
                    #camera.stop_preview()
                end=perf_counter()
                
                print("count", count)
                frame_rate = count/(end-start)
                print("frame rate", frame_rate)
                print("end", time_end)
                break
        except KeyboardInterrupt:
            print("Interrupt")
            break
 
    else:
        break
# Quit the program...    
quit() 
