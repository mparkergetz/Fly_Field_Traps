#! /bin/bash

scp flyranch@[IPADDRESS]:~/repositories/Fly_Field_Traps/Software/Image_Acquisition/control.json ~/Field_Trap


sudo gpsd /dev/serial0 -F /var/run/gpsd.sock

cd Field_Trap
nohup python3 gpsdatatext.py &


