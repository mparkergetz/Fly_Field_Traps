# Start Up Protocol

## Step 1: Power Pis
* First start by powering the pis with the portable batteries with the 5v port using a Micro-USB

## Step 2: Ethernet or Set Up Network
* If utilizing Direct Ethernet connection then all that needs to be done
is plugging each individual pi to the Lab laptop.

* If Setting up Network...
    * Make sure beforehand that the pis can connect to this network on boot
    * After powering the pis and waiting 1 minute to ensure that the pis have connected then connect the laptop to the same network

## Step 3: SSH into Pis
* Determine the IP Address for the Pi running the following

    ` ping raspberrypi.local `

* Now knowing the IP Address for the Pi ssh into the pi (it is understood that the user knows the pi's username and password)

    ` ssh pi@[IPADDRESS] `

## Step 4: Run Start-Up Bash Script
* Execute the start_exp.sh in order to initialize the GPS on serial port 0

    ` ./start_exp.sh `

* This will initialize but also run gpsdatatext.py and save the gpsdata to a text file

* You can go to the following directory on the pi to determine whether or not the pi is recieving the GPS information

    `cd Field_Trap/GPS_data/YYYY-MMM-DD`

## Step 5: RTC Time Check
* Will need to verify the RTC time to current time to ensure that the RTC clock is working appropriately.
    * This needs to be done before leaving for the field experiment, but also before starting the field experiment as a double check

    ` sudo hwclock -r `

## Step 6: Set Experiment Start Time and Duration
* The Set_Control.py script will be run to set framerate, start time and duration.
Saves to a json file.
    * Give youself some extra time to run 1 or 2 test images before starting the experiment

    ` cd Field_Trap/Image_Acquisition `
    ` python3 Set_Control.py `

## Step 7: Run Test Image
* Before the start the experiment take a test image with the following command
    * This is assuming that you are within the same Image_Acquistion directory

    ` cd Field_Trap/Image_Acquisition `
    ` python3 Field_Trap.py -t`

* After running proceed to check the following directory for the image 
` cd Field_Trap/Image_Acquisition/images/test_images`
                        OR
` cd Field_Trap/Image_Acquisition/images/timelapse`

## Step 8: File Transfer
* **THIS PROCESSES WILL BE AUTOMATED BUT FOR NOW USE THE FOLLOWING**

* FOLDER SCP IS NOT CURRENTLY WORKING....

* For a single file to current directory on laptop:
    ` scp pi@[IPADDRESS]:~/Field_Trap/Image_Acquisition/images/timelapse/STARTIME/FILENAME.jpg . `

* For the contents of an entire directory to specific directory on laptops:

    ` scp -r pi@[IPADDRESS]: ~/Field_Trap/Image_Acquisition/images/timelapse/STARTTIME /Desktop/images/STARTTIME `

Example:
scp pi@10.42.0.198:~/Field_Trap/Image_Acquisition/images/test_images/2022-07-18/20220718145122.540588.jpg .