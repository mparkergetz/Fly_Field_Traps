# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Editted by Logan Rower to add functionality to have a csv file for each experiment with the data
"""
This script is meant to create a csv file for each test in order to get reading on 
how accurate the GPS coordinates are with the current module over time

Last Editted:  7/12/2022 by Logan Rower
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
import pandas as pd

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
path = "/home/pi/Desktop/Field_Trap/GPS_data/"
start_time = datetime.now() # will use start time when we are in the end making the csv file for the experiment...
print(start_time)

# Set the time to end the experiment
## Experiment runs for 5 minutes
tdelta =  timedelta(minutes = 5)
end_time = start_time +tdelta

print(f"End time:{end_time}")

# created the folder for the start date
gps_fold_name = str(start_time.strftime("%Y-%m-%d"))
path_new = os.path.join(path,gps_fold_name )
os.makedirs(path_new, exist_ok = True)

# initial time
last_print = int(start_time.strftime("%Y%m%d%H%M%S"))

# Set up a dictionary and then converted to a dataframe
# # that will be used to house both the time series data as well as the lat and long data
lat_data = []
long_data = []
time_series = [] # recorded in seconds (will run experiment for 5 minutes...)

gps_dict = {
    "lat" : lat_data,
    "long": long_data,
    "time": time_series
}

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

    # SEND TO THE DICTIONARY:
    gps_dict['lat'].append(lat)
    gps_dict['long'].append(lon)
    gps_dict['time'].append(diff_sec)
    print(datetime.now())
    if datetime.now() >= end_time:
        break

# continues through while loop until end time reached or until control c...
# converted to dataframe after breaking out of loop
df = pd.DataFrame.from_dict(gps_dict)
location = path_new + "/%s.csv"
filepath = location % start_time.strftime("%Y%m%d%H%M%S")
# saves csv file to the folder..
df.to_csv(filepath, index=False)
