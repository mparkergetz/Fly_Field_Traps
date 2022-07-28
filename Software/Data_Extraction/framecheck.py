# This script seeks to determine whether there were skipped frames
# Using the preset JSON File the frame rate can be determined.
# The date of experimental release will need to be inputted by the user..

import numpy as np
import os
import sys
date = input("Input the Date of Release (YYYY-MM-DD")
pi_num = input("Input the Pi Number: ")
release_time = input("Release Precise Time (YYYYMMDDHHMMSS)")
timelapse_fold = pi_num+'_'+release_time
path = '/media/flyranch/Samsung_T5/Field_Trap_Exps/'+date+'/'+timelapse_fold

# change directory to this directory
os.chdir(path)

# now within the timelapse directory we need to check to see if all files minus the first are in increments of
# the framerate... in this case 2 seconds.

https://www.geeksforgeeks.org/python-list-files-in-a-directory/


