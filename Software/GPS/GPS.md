
Python Base Code Source:
* https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage


## Installations for GPS Time Series (IN ORDER)
* sudo pip3 install adafruit-circuitpython-gps
* sudo apt-get install python3-numpy
    - needed to update numpy to latest version
* (FOR BUSTER) sudo apt-get autoremove
    - removed teh libdav1d3 library after installing new numpy
* sudo apt-get install python3-pandas


# GPS Time Series Protocol:
1. Connect the pi and laptop either to the same network or via ethernet
2. once connected via ssh into the pis then use the command below to find the local pis ip addresses on the network if it is unknown
    ping raspberrypi.local
3. Then once connected to the pi run the following command
    nohup python3 gpsdata.py &
4. Then control c
5. Then exit out of ssh
6. Then after the timer you have set for 5 minutes has elapsed the script will be completed. The following will be used for both pis to copy
the files over the the laptop or desktop

scp pi[IPADDRESS]:~/Desktop/Field_Trap/GPS_data/YYYY-MM-DD/FILENAME.csv .

The period signifies the current working directory that you are in on the laptop/desktop

7. Once this command has been sent you can view the copied fiel and graph the gps coordinates over time. 
This will allow the determination for how effective the device was and whether it will be adequate for further experiments.

