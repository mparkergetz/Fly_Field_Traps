# This script seeks to determine whether there were skipped frames
# Using the preset JSON File the frame rate can be determined.
# The date of experimental release will need to be inputted by the user..

import numpy as np
import os
import sys
from datetime import datetime
#date = input("Input the Date of Release (YYYY-MM-DD")
#pi_num = input("Input the Pi Number: ")
#release_time = input("Release Precise Time (YYYYMMDDHHMMSS)")
#timelapse_fold = pi_num+'_'+release_time
#path = '/media/flyranch/Samsung_T5/Field_Trap_Exps/'+date+'/'+timelapse_fold
#path_log = \
# change directory to this directory
## FOR WINDOWS MACHINE DO DIFFERENTLY FOR LINUX...
#### USER INPUTS THE DATE OF THE EXPERIMENTAL RELEASE
os.chdir(r"C:\Users\lkrow\Desktop")
# THEN WE HAVE THE USER INPUT FOR THE FOLDER NAME:
### SPECIFIC RELEASE TIME.
dir_list=os.listdir("Pi1_20220728141153")
# print(dir_list[0][4:18]) ### Original (WILL BE OMITTED...)

# WITH THE FOLDER NAME WE CAN THEN LOOP THROUGH TO DETERMINE IF THE FILENAMES ARE IN INCREMENTS OF 2...
## FIRST DELETE THE FIRST FILE....
### Resaved the list to be without first index..
dir_list = dir_list[1:]
# print(dir_list[0][4:19]) # ACTUAL FIRST FRAME...
# time = dir_list[0][4:19]
# print(time)
# dt_obj = datetime.strptime(time,'%Y%m%d_%H%M%S')
# print(dt_obj)
## SECOND:
"""
Next a for loop is generated that will take the next index and take absolute value diff of the first with both times first being converted
into datetime objects from the string and then determine whether there is a difference of 2 between the two times. If so then continue, but
if not then the count is saved for the number of missed frames.

4:18 is the range of the filename associated with the time.

time = dir_list[0][4:18]
dt_obj = datetime.strptime(time,'%Y%m%d_%H%M%S') <- How to structure format to switch from string to datetime object

"""
num_off = []
print(len(dir_list))
for file_num in range(0, len(dir_list)):
    # got the time image was taken
    if file_num >= 1:
        imgt_current = datetime.strptime(dir_list[file_num][4:19],'%Y%m%d_%H%M%S')
        imgt_prev = datetime.strptime(dir_list[file_num-1][4:19],'%Y%m%d_%H%M%S')
        duration = imgt_current - imgt_prev
        t_rate = duration.total_seconds()
        #print(t_rate)
        if t_rate == 2:
            continue
        else: 
            num_off.append([file_num -1, file_num])

    else:
        continue
print(num_off)
print(len(num_off))
# now within the timelapse directory we need to check to see if all files minus the first are in increments of
# the framerate..d. in this case 2 seconds.
for num in num_off:
    for sub_num in num:

        # THIS PRINTS OUT THE FILES THAT ARE OFF...
        print(dir_list[sub_num][4:19]) 

        # So between four images is what created problems.. (99.78% success rate with the camera framerate)



