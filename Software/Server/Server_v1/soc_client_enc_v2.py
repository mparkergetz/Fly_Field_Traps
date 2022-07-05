#!/usr/bin/env python3
# FOR UBUNTU include the above line...
"""
This works in essentially creating a client that will 
1. Send a Message that it has connected
2. Send a message that it has disconnected

It does this in a way through encoding the strings so they can be properly 
sent...

"""
## Serial on
## ssh On
## VNC ON
## Connect to the network created by the Hub pi
from lib2to3.pytree import convert
import socket
import threading
import time
import base64
import os
import codecs
# 60 seconds for pi
time.sleep(60)
HEADER =  64 # bytes

# Set arbritrary port number
## will need to be different if on pi...
## PI HUB PORT
### Using PiHub works as the server....
### CAn try toi use VNC viewer or SSH to utilize the pi..

## Port for the Ubuntu Machine
PORT = 5050


DISCONNECT_MESSAGE = "!Disconnect"

# Hub Pi Server:
#SERVER = '192.168.220.1'

#Laptop Server PIAP
SERVER = '192.168.220.91'

#SERVER FOR UBUNTU MACHINE (LOGAN's HOME)
#SERVER = '192.168.86.129'
# SERVER FOR UBUNTU MACHINE (LOGAN'S LAPTOP ON PIAP)
#SERVER = '192.168.220.60'
ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

# SOCKET SET UP! for client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

# # HAVE NOT TESTED SENDING A MESSAGE BUT WE ARE ABLE TO ESTABLISH A CONNECTION!!

# def send(msg):
#     """
#     Now the message will be sent to the server from the client
#     """
#     message = msg.encode(FORMAT) # encode as a byte format..
#     # length of message
#     msg_length=len(message)
#     # now will send the ecoded length
#     #
#     send_length = str(msg_length).encode(FORMAT)
#     # and will pad in order for it to make it to 64 bytes..
#     ## adds the additional amount needed in order to get to 64 byte
#     send_length += b' ' * (HEADER- len(send_length))

#     # then will send the message length and the message
#     client.send(send_length)
#     client.send(message)

# send("Hello World!")
# time.sleep(30)
# send(DISCONNECT_MESSAGE)
print("Recieving..")
data = client.recv(1024)
print("Decoding...")
msg = data.decode(FORMAT)
print(f"Data: {msg}")

# Now determine whether or not the message will perform the experiment or it will send an image
## In this case the image is a preset one

## https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
if msg == "Single Image":
    """
    ENCODING ISSUE IS IN HERE.... NEED TO USE DIFF METHODS:

    1. https://www.adamsmith.haus/python/answers/how-to-convert-an-image-to-a-string-in-python
    2. https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
    3. https://www.geeksforgeeks.org/python-pil-tobytes-method/
    4. https://pillow.readthedocs.io/en/stable/reference/Image.html
    5. 

    USEING THIS>>>>

    https://www.codegrepper.com/code-examples/python/python+send+image+server



    """
    filename = "4kelephant.jpg"
    img = open (filename,"rb")
    size = os.path.getsize(filename)
    #print(type(size))
    bytes_send = img.read(size)
    #print(type(bytes_send))
    byte_length = str(size)
    #byte_len_check = len(str(bytes_send, FORMAT))

    # Send the length of the byte string,.
    #client.send(bytes(byte_length,FORMAT))

    # First Send the image bytes once and these will be converted into a length by the server
    #client.sendall(bytes_send)
    ## Check The Lengths:
    print(f"bytes size:{byte_length}|| bytes check: {len(bytes_send)}")
    # if byte_length==len(bytes_send):
        # Then will send all of the image bytes...
    client.sendall(bytes_send)
    # CORRECT SIZE BYTES HAVE BEEN SENT!!!
    img.close()
    print("IMG SENT!")
#     with open ("windtunnel.jpg","rb") as image2string:
#         binary_data = image2string.read()
#         print(f"Binary data:{binary_data}")
#         base64_encoded_data = base64.b64encode(binary_data)
#         base64_decoded_data = base64.b64decode(base64_encoded_data)
#         #str_data = base64_encoded_data.decode(FORMAT)
#         #print(str_data)
#         #print(type(base64_encoded_data))
#         #base64_message = base64_encoded_data.encode(FORMAT)
#         #base64_message = base64_encoded_data.decode('utf-8')
#         # converted_string = base64.b64encode(image2string.read())
#         #print(base64_message)
#         #base64_msg= converted_string.decode('utf-8')
#         #message_bytes = base64.b64decode(base64_bytes)
#         #print(base64_encoded_data)
#         #print(len(str_data))
#         length = str(len(str_data))
#         # Send the length of the binary string
#         client.send(length.encode(FORMAT))

#         bytes_sent = 0
#         print(len(binary_data))
#         print(len(base64_encoded_data))
#         while bytes_sent < int(length):
#             bytes_sent += client.send(bytes(str_data, FORMAT))
#             print(f"Bytes Sent: {bytes_sent} || Length: {int(length)}")
#             # if bytes_sent > int(length):
#             #     break
#         print("I AM FREE")
# # USE SCP... Then we can then use python to basically take this..
# ## Secure Copy with Python...using this with the Target IP Address and the Target Directory
# ##

