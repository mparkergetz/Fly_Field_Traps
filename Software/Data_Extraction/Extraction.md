# Data Extraction from Pi's

## Version 1: Single Scp from JSON of IPs

In order to extract the data from the pis a bash script will be utilized. This bash script will have a list of all of the IP addresses from a json file that has been created that has all of the pi IP addresses and the shorthand "Pi Number" (Ex: Pi1). Then it will run this specific Pi that has been assigned an IP address.

In order to do to this jq will need to be installed using the following methods
* https://installati.one/ubuntu/20.04/jq/


Using jq
https://linuxconfig.org/how-to-parse-a-json-file-from-linux-command-line-using-jq

removing string quotes:
https://tecadmin.net/bash-remove-double-quote-string/

IMPORTANT:
The ip_list.json file and the extract.sh should be located on a seperate location on the laptop such that the IP addresses are not uploaded with each commit...

Bash Script Structure:
* There will be a json file will all of the Pis numbered as keys and the values are the IP Address
* Then the User will input something that will be the key
* Then the bash script will essentially grab the value associated with the key and then remove the quotes around the IP address.
* Then this value will be inserted as a variable into the scp command




What will happen is the user will input the pi number... lets say it is Pi 1

Then the user inputs  Pi 1 into the command line then a specifc command is run for Pi 1 and it grabs it and then it will run the scp based on the IP address that it got from this...


## Version 2: Quick SCP over Socket Connection!

scp protocol for each of the IP address for todays date. This will get the newest folder will all data for today onto the local machine.

Need a list of all of the IP Addresses on the local network to put into a file that will reside on the Main Laptop...


