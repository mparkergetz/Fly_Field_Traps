# Start Up Protocol

## Step 1: Power Pis
* First start by powering the pis with the portable batteries with the 5v port using a Micro-USB

## Step 2: Ethernet or Set Up Network
* If utilizing Direct Ethernet connection then all that needs to be done
is plugging each individual pi to the Lab laptop.

* If Setting up Network...
    * Make sure beforehand that the pis can connect to this network on boot
    * After powering the pis and waiting 1 minute to ensure that the pis have connected then connect the laptop to the same network

* May have to open the known_hosts file on the laptop and delete the listed entry if there is an error regarding the "known host". Since
this is likely due to the fact that the IP address you are trying to use was utilized for something else previously.
    * All that is needed is to go into this "known_hosts" file and delete the line is referenced.

## Step 3: Test Image on Pi through RealVNC
* Determine the IP Address for the Pi running the following in the terminal

    ` ping raspberrypi.local `

* Now knowing the IP Address for the Pi open VNC Viewer on the laptop and select the pi device with the appropriate IP address (it is understood that the user knows the pi's username and password)

* User can also ssh into the pi using the following terminal command:

    ` ssh pi@[IPADDRESS] `

* to run a test image on the pi go to the following directory

    `cd Field_Trap/

* now execute the following command

    `python3 Field_Trap.py -t `
    
    OR IF AN HQ CAMERA (Telephoto or Wide Angle Lens)

    `python3 Field_Trap_HQ.py -t `

## Step 4: Check the RTC Time 
* Will need to verify the RTC time to current time to ensure that the RTC clock is working appropriately.
    * This needs to be done before leaving for the field experiment, but also before starting the field experiment as a double check

    ` sudo hwclock -r `

## Step 5: Update control.json file on laptop 
* Disconnect from the VNC Viewer if you haven't already and proceed to the terminal to run the Set_Control.py script
    * This will update the control.json file on the the laptop that will be extracted to the pi follow the below steps to do this...
* Go to the following directory:

    ` cd ~/repositories/Fly_Field_Traps/Software/Image_Acquisition`

* Run the following python command 
    * (be mindful that this control file is what will be used for each pi unless you change it before running the experiment on the pi)

    ` python3 Set_Control.py`

* *Note that to update to pi, the .json file needs to be transferred to pi as detailed in next step*

## Step 6: Run Start-Up Bash Script
* Now that the control.json file has been updated with the appropriate time and duration you can then ssh into the pi device from the terminal

    ` ssh pi@[IPADDRESS] `

* Execute the start_exp.sh in order to pull the current control.json file, initialize the GPS on serial port 0, and start the timelapse and GPS scripts in the background 
    * with timelapse starting at x time (defined in control.json) and GPS going for x minutes
    * gps data will be saved to a textfile, and the timelapse will record image files to a folder.

    ` ./start_exp.sh `

        * You will see something like this: "nohup: nohup: ignoring input and appending output to 'nohup.out'appending output to 'nohup.out'"
        When this appears wait 15 seconds to make sure that both files are in the background and then Ctrl-C out.

* exit out of the pi device

* You can ssh back into the pi and go to the following directory on the pi to determine whether or not the pi is recieving the GPS information

    `cd Field_Trap/GPS_data/YYYY-MMM-DD`

* When the experiment starts you can go to the following directory on the pi to determine whether the pi is saving images

    `cd Field_Trap/Image_Acquisition/images/timelapse/YYYY-MMM-DD`

    `more STARTTIME`


## Step 7: File Transfer
* In order to perform this file transfer method the ip_list.json needs to be finalized with all IP addresses from the Pis

* In the Terminal go to the following directory on the laptop

    `cd ~/repositories/Fly_Field_Traps/Software/Data_Extraction`

* After inputting this command run the following bash script to start the file transfer process (for the current date)

    `./extract.sh`
    
    * If this bash script does not run then do `chmod +x extract.sh` in order to make it an executable

* The bash script will require the user to input the Pi Number which would be in range of "Pi1" to Pi9". The Pis will be labelled with the appropriate number...

* The script will then take the current date and find the directory corresponding to the current date. As such it will copy everything within it and transfer it over. This means that if multiple tests were run in a day then all the user would need to do is run this script again after that test was completed. Then a new folder for the start time of the experiment will be generated.

    * scp is used to transfer the files and jq is used in order to grab the IP Address out of the json file.


### 7/22/2022
* Pis Status:
    - Pi1 -> Image: GOOD, GPS: GOOD
    - Pi2 -> Image: GOOD, GPS: GOOD
    - Pi3 -> Image: GOOD, GPS: NONE
    - Pi4 -> Image: GOOD, GPS: GOOD
    - Pi5 -> Image: GOOD, GPS: GOOD
    - Pi7 -> Image: GOOD, GPS: GOOD
    - Pi8 -> Image: GOOD, GPS: GOOD
    - Pi9 -> Image: GOOD, GPS: GOOD


* NEED TO HAVE OPENSSH INSTALLED ON LAPTOP FOR THIS TO WORK TO DO SCP ...
* Alignment of the Box Traps should be such that the handles are not facing the inner or outer sides of the 80/20 tripod stand