# Software Notes:

> The software for the camera traps has three aspects. 

> The first, is the methodology utilized with initial start-up of the scripts on all of the pis

> The second, is the control script for each pi that controls both the camera, and relevant points of data aquisition (ex: GPS). At this point in time image data is the only relevant data being transferred and aquired

> The final stage is the image transfer... (SSH option), utilizing python socket.io to create a web server that will have the most recent images. 

## Start up
* The start up will be done utilizing a bash script.
* The raspberry pi that will be considered to be the "host" for the local internet by creating a wifi access point will be utilized as the the host for the experiments. This pi will not be taking images. And all of the processing power will be for driving the access point, and for running the inital script.
* The initial script could be run either on the host pi or on the desktop
* This script will be developed based on the below resources....
   * https://www.raspberrypi.com/documentation/computers/remote-access.
   * https://raspberrytips.com/ssh-guide-raspberry-pi/
   * 

* This script will first ssh into all the pis (need their IP addresses). Then after that point it will 


## Using ROS with Raspberry Pis?