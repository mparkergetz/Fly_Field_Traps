# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Editted by Logan Rower to add functionality to have a csv file for each experiment with the data


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
gps.send_command(b"PMTK220,1000")
# Or decrease to once every two seconds by doubling the millisecond value.
# Be sure to also increase your UART timeout above!
# gps.send_command(b'PMTK220,2000')
# You can also speed up the rate, but don't go too fast or else you can lose
# data during parsing.  This would be twice a second (2hz, 500ms delay):
# gps.send_command(b'PMTK220,500')

# First set up the folder that will essentially be responsible for holding the data for 
## The Day in which experiments took place. Then csv files will be saved based on the start time of the experiment
path = "/home/pi/Desktop/Field_Trap/GPS_data"
start_time = datetime.now() # will use start time when we are in the end making the csv file for the experiment...
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

counter_start = time.perf_counter()
while True:
    try:
        # Make sure to call gps.update() every loop iteration and at least twice
        # as fast as data comes from the GPS unit (usually every second).
        # This returns a bool that's true if it parsed new data (you can ignore it
        # though if you don't care and instead look at the has_fix property).
        gps.update()
        # Every second print out current location details if there's a fix.
        # Also will save to a new file in the directory GPS_DATA
        current = datetime.now()
        if int(current.strftime("%Y%m%d%H%M%S")) - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                print("Waiting for fix...")
                continue
            # We have a fix! (gps.has_fix is true)
            # Print out details about the fix like location, date, etc.
            print("=" * 40)  # Print a separator line.
            

            # Record the time difference from the start
            diff = (current - start_time)
            diff_sec =int(diff.total_seconds())
            # gps long and lat
            lat = gps.latitude
            long = gps.longitude
            print (current.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"Seconds: {diff_sec} s")
            print("Latitude: {0:.6f} degrees".format(gps.latitude))
            print("Longitude: {0:.6f} degrees".format(gps.longitude))
            
            print("Fix quality: {}".format(gps.fix_quality))


            # SEND TO THE DICTIONARY:
            gps_dict['lat'].append(lat)
            gps_dict['long'].append(long)
            gps_dict['time'].append(diff_sec)

            # continues through while loop until end time reached or until control c...
    except KeyboardInterrupt: 
        break

# converted to dataframe after breaking out of loop
df = pd.DataFrame.from_dict(gps_dict)
location = path_new + "/%s.csv"
filepath = location + start_time.strftime("%Y%m%d%H%M%S")
# saves csv file to the folder..
df.to_csv(filepath, index=False)

        # # Some attributes beyond latitude, longitude and timestamp are optional
        # # and might not be present.  Check if they're None before trying to use!
        # if gps.track_angle_deg is not None:
        #     print("Track angle: {} degrees".format(gps.track_angle_deg))
        # if gps.horizontal_dilution is not None:
        #     print("Horizontal dilution: {}".format(gps.horizontal_dilution))
