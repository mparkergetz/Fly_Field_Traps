#!/usr/bin/env python3

import socket
import threading

# SERVER WILL FIRST LET THE USER WHETHER DEVICES HAVE CONNECTED...
## WIll need to configure the pis to give them each a number instead of referencing IP ADDRESS.

# SERVER Will then have the user decide between sending the command 
# to initiate the experiment 1 on the pis, or do a test image check
# on each of the pis. The experiment will last a predetermined amount of time

# USER will then run the kill command which will kill whaterve current process
# is happening...

HEADER =  64
PORT = 5050
#IP Address for SERVER OF THE UBUNTU MACHINE
SERVER = '192.168.220.91'
# ADDR: address that we will use to bind to the socket
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

# Disconnection Message
DISCONNECT_MESSAGE = "!Disconnect"

# Initialized the Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV6 addresses..., Steaming Data 

# bind socket to the address....
server.bind(ADDR)

# 