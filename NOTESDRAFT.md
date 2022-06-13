## Bash Script Start up Thought Process....
* The start up will be done utilizing a bash script.
* The raspberry pi that will be considered to be the "host" for the local internet by creating a wifi access point will be utilized as the the host for the experiments. This pi will not be taking images. And all of the processing power will be for driving the access point, and for running the inital script.
* The initial script could be run either on the host pi or on the desktop
* This script will be developed based on the below resources....
   * https://www.raspberrypi.com/documentation/computers/remote-access.
   * https://raspberrytips.com/ssh-guide-raspberry-pi/
   * 
* This script will first ssh into all the pis (need their IP addresses). Then after that point it will 

## More ideas and sources
* https://forums.raspberrypi.com/viewtopic.php?t=162873
* File Sync
    * https://raspberrypi-guide.github.io/filesharing/file-synchronisation-rsync-rclone
* Pi and Arduino Serial Communication
    * https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/

* Public and Private Keys
    * https://help.ubuntu.com/community/SSH/OpenSSH/Keys

* Cluster Computing with 3 Pis
    * https://magpi.raspberrypi.com/articles/cluster-computer-raspberry-pi-3

* MPI for Python
    * Message Passing Interface 
    * https://mpi4py.readthedocs.io/en/stable/


## File Transfer IDEAS:

* Rsync
    * Use this for over SSH  to transfer files to computer automatically. (Image from Pi -> Laptop/Desktop)

* Mount/Unmount:
    * This could basically make a certain directory accessible and then can then unmount it from the network when done...
        * Could be good then all info is stored on the laptop!...
        * All data is transferred off of pis...
        * Issue with this is that all pis would likely transfer data into a particular folder and that folder would be pi specific...



<!-- * Wireless Communication Between Raspberry Pi and Your Computer
    * https://spin.atomicobject.com/2013/04/22/raspberry-pi-wireless-communication/ -->

