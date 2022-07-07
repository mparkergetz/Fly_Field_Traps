# Set Up of the Field Trap Software

## Enabling Ethernet Connectivity to Pis 
This was done by enabling ssh on the pis, and avoiding any other complex
methods. See the Raspberry Pi Troubleshooting for more on Ethernet Connection

## Connect to the Pi via Ethernet connection
This is done so that the internet connection on the laptop can be utilized in order to perfom installations onto the raspberry pi.

## Soldering
* soldering header on the GPS unit

## 

## Witty Pi Software Installation
Once you are connected to internet perform the following commands
These are from the documentation from UUGear regarding Witty Pi 3 software installation.

wget http://www.uugear.com/repo/WittyPi3/install.sh

sudo sh install .sh

After you have ran these commands shut the pi down:
sudo shutdown -h now