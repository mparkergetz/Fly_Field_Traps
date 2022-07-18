#! /bin/bash
sudo gpsd /dev/serial0 -F /var/run/gpsd.sock

cd Field_Trap
python3 gpsdatatext.py