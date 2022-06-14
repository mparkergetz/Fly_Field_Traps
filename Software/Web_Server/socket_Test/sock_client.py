#!/usr/bin/env python3
import socket



HEADER =  64 # bytes

# Set arbritrary port number
## will need to be different if on pi...
## SAME AS IN SERVER>>>
PORT = 8080

DISCONNECT_MESSAGE = "!Disconnect"

# Different SERVER...
SERVER = '127.0.1.1'

ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

# SOCKET SET UP! for client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    """
    Now the message will be sent to the server from the client
    """
    message = msg.encode(FORMAT) # encode as a byte format..
    # length of message
    msg_length=len(message)
    # now will send the ecoded length
    #
    send_length = str(msg_length).encode(FORMAT)
    # and will pad in order for it to make it to 64 bytes..
    ## adds the additional amount needed in order to get to 64 byte
    send_length += b' ' *(HEADER- len(send_length))

    # then will send the message length and the message
    client.send(send_length)
    client.send(message)

send("Hello World!")
input()
send(DISCONNECT_MESSAGE)