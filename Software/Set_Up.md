# Set Up of the Field Trap Software

## Enabling Ethernet Connectivity to Pis 
This was done by enabling ssh on the pis, and avoiding any other complex
methods. See the Raspberry Pi Troubleshooting for more on Ethernet Connection

## Connect to the Pi via Ethernet connection
This is done so that the internet connection on the laptop can be utilized in order to perfom installations onto the raspberry pi.

## Soldering
* soldering header on the GPS unit

## RTC Set Up
* First the 

## Witty Pi Software Installation
Once you are connected to internet perform the following commands
These are from the documentation from UUGear regarding Witty Pi 3 software installation.

wget http://www.uugear.com/repo/WittyPi3/install.sh

sudo sh install .sh

After you have ran these commands shut the pi down:
sudo shutdown -h now



# Start Up Documentation 

##
> Need a clean Raspberry Pi OS Buster April 2022 version (Latest Version should work)

> 


## Network Set Up

> The pi's and other devices will all be connected to the same local network. This is through setting up one pi as a wifi access point



* See repository for file copies for installation of the OS onto an SD card 

> See the below resource for setting up this wireless access point: 
* https://pimylifeup.com/raspberry-pi-wireless-access-point/

> Test the that the wifi access point works for both pis and other devices for wireless ssh..

> Password to get into accesspoint = raspberry

## Bash Start Up:
* First will initialize serial port 0 to recieve the GPS information. 
* Will then run the gpsdata script
