# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Editted by Logan Rower to add functionality to have a csv file for each experiment with the data
"""
This script is meant to continuosuly write to a text file..

how accurate the GPS coordinates are with the current module over time

Last Editted:  7/22/2022 by Logan Rower
- For Pi1 but can be editted for other pis such that file and folder names
are labeled for the experiment starttime and with the specific pi number the data
is from
"""

# Simple GPS module demonstration.
# Will wait for a fix and print a message every second with the current location
# and other details.
import time
from tracemalloc import start
import board
import busio
from datetime import datetime, timedelta
import adafruit_gps
import os
#import pandas as pd

# Create a serial connection for the GPS connection using default speed and
# a slightly higher timeout (GPS modules typically update once a second).
# These are the defaults you should use for the GPS FeatherWing.
# For other boards set RX = GPS module TX, and TX = GPS module RX pins.
#uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

# for a computer, use the pyserial library for uart access
import serial
## Port is serial0 as intialized before..
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)

# If using I2C, we'll create an I2C interface to talk to using default pins
# i2c = board.I2C()

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
# gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface

# Initialize the GPS module by changing what data it sends and at what rate.
# These are NMEA extensions for PMTK_314_SET_NMEA_OUTPUT and
# PMTK_220_SET_NMEA_UPDATERATE but you can send anything from here to adjust
# the GPS module behavior:
#   https://cdn-shop.adafruit.com/datasheets/PMTK_A11.pdf
# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Turn on just minimum info (RMC only, location):
# gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Turn off everything:
# gps.send_command(b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Turn on everything (not all of it is parsed!)
# gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,5000")
# Or decrease to once every two seconds by doubling the millisecond value.
# Be sure to also increase your UART timeout above!
# gps.send_command(b'PMTK220,2000')
# You can also speed up the rate, but don't go too fast or else you can lose
# data during parsing.  This would be twice a second (2hz, 500ms delay):
# gps.send_command(b'PMTK220,500')
time.sleep(5)
# First set up the folder that will essentially be responsible for holding the data for
## The Day in which experiments took place. Then csv files will be saved based on the start time of the experiment
path = "/home/pi/Field_Trap/GPS_data/"

# load the json file in
with open('control.json') as json_file:
    control_data = json.load(json_file)
start_time = control_data['start_time']
duration = control_data['duration']

# set the duration (SET IN JSON)
time_hr = duration[0]
time_min = duration[1]
time_sec = duration[2]

# Set the time to end the experiment
## Experiment runs for 5 minutes
tdelta = timedelta(seconds = time_sec, minutes = time_min, hours = time_hr)
end_time = start_time +tdelta

print(f"End time:{end_time}")

# created the folder for the start date
gps_fold_name ="Pi1_"+start_time.strftime("%Y%m%d%H%M%S")
path_new = os.path.join(path,gps_fold_name )
os.makedirs(path_new, exist_ok = True)

# initial time
last_print = int(start_time.strftime("%Y%m%d%H%M%S"))

# Set up a dictionary and then converted to a dataframe
# # that will be used to house both the time series data as well as the lat and long data
# recorded time in seconds (will run experiment for 5 minutes...)

location = path_new + "/Pi1_%s.txt"
filepath = location % start_time.strftime("%Y%m%d%H%M%S")
if current_time >= start_time:
    with open(filepath, 'w') as writer:
        while True:
            # Make sure to call gps.update() every loop iteration and at least twice
            # as fast as data comes from the GPS unit (usually every second).
            # This returns a bool that's true if it parsed new data (you can ignore it
            # though if you don't care and instead look at the has_fix property).
            time.sleep(5)
            gps.update()
            # Every second print out current location details if there's a fix.
            # Also will save to a new file in the directory GPS_DATA
            current = datetime.now()
            diff = (current - start_time)
            diff_sec =int(diff.total_seconds())
            # gps long and lat
            lat = gps.latitude
            lon = gps.longitude

            # saves data to the text file to the folder..
            writer.write(str(diff_sec)+" "+str(lat)+" "+str(lon)+"\n")
            # continues through while loop until end time reached
            print(datetime.now())
            if datetime.now() >= end_time:
                break