#!/usr/bin/env python3
# 6/15/2022 USE THIS VERSION!
import socket
import threading
from tkinter import Image
import numpy as np
import base64
import time
import codecs
"""


It is important to note the the user will not be able to automatically start everything and that
the user will have to manually parse through each of the pi devices for additional checks and in order to start the time
* TRY TO CHANGE LATER... (MAKE SO THAT CAN DO ONE COMMAND TO SEND OUT ALL OF THE THREADS...)

Functions:
1. Listener Function:
 This will connect the device to the server and the server will display the indicaiton as such
 Additionally the IP and Port of the device is stored in  <- MAYBE???

2. Single Image will be Sent from Client to Server
    This is done by the server sending a particular message to the client to perform a function
3. Experiment will be run on client by server communicating to client...
    This is done by the server sending a particular message to the client to perform a function
    Start Time of the experiment will be sent to all of the clients..
4. Finally the main_function is used in order to group the threading functions and run them as needed..
5. Disconnection Function <- IN main_function?


6/22/22 NOTES:

SCP TEST THIS OUT... Th

AT ANY TIME... USER NEEDS TO KNOW FRAMS PER SECOND...-> 

USER NEEDS TO BE ABLE TO SEE LIVE IMAGE ON THE FEED... ??? 
SO THEN WE WOULD NEED TO BE ABLE TO GO INTO A PI DEVICE AND THEN CHECK TO SEE HOW
THE AQUISITION IS GOING..

BEFORE STARTING THE CONNECTIONS... THE SERVER NEEDS TO START THEN AFTER ALL THE CLIENTS HAVE STARTED THEN
WILL HAVE THE SERVER SEARCH FOR CONNECTIONS....

NEED TO IMPLEMENT THE GPS FUNCTIONALITY...AND SAVE THE GPS to a TXT file and
only save this at the start...

6/23/22

Client to Server Sending of Image via bytes seems to work very well

NEED TO MAKE A DICTIONARY OF CLIENT CONN AND ADDR...
-> SO THEN THIS WAY WE CAN EFFICIENTLY GO BACK AND ISSUE COMMANDS AFTER FIRST CONNECTING TO ALL THE CLIENTS..

"""


# REFERENCES
# https://www.geeksforgeeks.org/python-program-that-sends-and-recieves-message-from-client/

HEADER =  64 # bytes

# Set arbritrary port number
## will need to be different if on pi...
PORT = 5050
#socket.getaddrinfo('localhost', 8080)
# Server by the IP Address of device hosting
#SERVER = socket.gethostbyname(socket.gethostname())

# SERVER FOR PI HUB
#SERVER = '192.168.220.1'

#SERVER FOR THE UBUNTU MACHINE (PIAP)
## This Stays Constant
SERVER = '192.168.220.91'

#SERVER FOR UBUNTU MACHINE (LOGAN's HOME)
#SERVER = '192.168.86.129'

# SERVER FOR UBUNTU MACHINE (LOGAN'S LAPTOP ON PIAP)
#SERVER = '192.168.220.60'

#print(SERVER)
# ADDR: address that we will use to bind to the socket
ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

# NEED TO Have 2 Threads (1 for Client and 1 for the listening Server?)
THREADS = 2 
# disconnect message
## when we recieve this message close client from server...
DISCONNECT_MESSAGE = "!Disconnect"
# Type of socket utilized for the server...
## Over internet.... -> Switch this method maybe?
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV6 addresses..., Steaming Data 

# bind socket to the address....
server.bind(ADDR)

# def listener_multi():
#     """

#     RUN THIS ONCE!

#     This function will establish the parameters of the CURRENT THREAD
#     The port and the IP address, and return them to be utilized in 
#     other functions where messages will be sent and recieved

#     This function will search for two clients and connect with them...


#     """
#     server.listen()
#     print("Server is listening on {SERVER} for new connections")
#     threads_init = threading.activeCount()
#     print("Initial number of threads: {threads_init}")
#     tot_threads = 1
#     clients = []
#     # For loop that will get the conn and addr for each of the clients...
#     for client in range(tot_threads):
#         print("Searching for Clients...")
#         # when new connection occurs this will be stored in this object here..
#         ## stores port and IP address of connection
#         conn, addr =  server.accept()
#         print(f"Connection {client + 1} accepted")
#         clients.append([conn, addr])
#     # List of the clients and their IP Addresses...
#     # The clients are now all connected 
#     return clients




# def handle_client(conn,addr):
#     """
#     handles communication between the client and the server

#     INDIVIDUAL CLIENT AND SERVER...


#     also deals with disconnection and reconnection... so reconnection it knows the client left...

#     GOOD FOR HANDLING ANY MESSAGES....
#     """

#     print(f"[New CONNECTION {addr} connected")
#     connected = True
#     while connected:
#         # message protocols need to figur eout...
#         ## will not run this code until a message is recieved from client..
#         ## how many bytes to recieve from client... using header...
#         # 1st message will be a message of length 64...will have number that will have length of number of bytes of what we are about to recieve.
#         ### then decode since encoded in byte format.. so decode from byte to string...
#         msg_length = conn.recv(HEADER).decode(FORMAT)
        
#         # Need to check to see if the message is a valid message..
#         ## since when we connect we don't get a valid message its basically blank

#         if msg_length:
#             # string to int..
#             msg_length = int(msg_length)
#             # now determine the number of byts we are recieveing for the actual message
#             msg= conn.recv(HEADER).decode(FORMAT)
            
#             if msg == DISCONNECT_MESSAGE:
#                 print(f"[{addr}]{msg}")
#                 connected = False
#             print(f"[{addr}]{msg}")
#     conn.close()


# First Threading Function: Single Image
## Using Image64 for byte conversion
def single_image(connection):
    """
    Sending single image from client to the server

    Server is going to tell the client to do this..

    Then the server is going to look for this...
    """
    connection.send(b'Send Single Image')
    # Have image save to particular directory per the experiment type...


# Second Threading Function: Run Experiment
##

# Main Function
## Run the two threading functions
#### Test Running one Thread at a Time by having the listener integrated so we need to have the thread manager as input functions
# or Running all the Threads in the for loop and then closing the connections and reopening them...
def thread_manager(connection, Address):
    """
    This function will manage the threads that are running

    Threads will run concurrently and not in parallel. User Inputs will slow program down

    User will be asked for what they want to do:

    Option 1: "Image_View" -> Maybe video/recording to make things easier for focusing?
        See what the current image on each of the camera traps...
        This will allow use to perform adjustments 
    
    Option 2: "Experiment" 
        Run the experiment and the user will provide the start time which will be sent to each of the 
    """

    # BASICALLY THIS WILL NEED TO RUN THROUGH EACH OF THE CLIENTS AND DETERMINE WHAT FUNCTION TO 
    # RUN BASED ON INPUT... 
    
    client = True
    while client == True:
        # DO a user input to determine the pathway that you want to go down..
            # PATH 1: Run the Image Viewer
            # PATH 2: Run Experiment
            # PATH 3: 
        print(" ALL Clients Loaded WHAT IS OUTPUT....")
        print("NEED INPUT....")
        test = int(input())
        if test == 1:
            start = time.perf_counter_ns()
            connection.send(bytes("Single Image", FORMAT))
            print("Recieving Image from Client..")
            # Will first recieve the length:
            # length = connection.recv(64)
            # print(type(length))
            #print(codecs.decode(length))
            # str_len_img = len(length)
            # print(str_len_img)
            #data = connection.recv(235328)
            # print(f"Length:{str_len_img}")
            # if str_len_img:
            flyimg = open("4kelephant2_new.jpg", 'wb')
            print("Recieve the Binary Image")
            #image = connection.recv(4096)
            print("Convert The Message to Image")
            current_length = 0
            # initialized bytes recieved as none..
            ## through the while loop with will be increased...
            ## The data from the recieve will be added to this variable
            bytes_recieved = None
            # Length of bytes...
            length_recieved = 0
            # The bytes recieved length will be examined continuously...
            while True:
                #while connection.recv(64):
                #new data from the connection with the image...
                image = connection.recv(4096)
                #print(f"Length of Recieved Bytes {len(image)}")
                length_recieved=len(image)
                #print(f"Length of Recieved Bytes {length_recieved}")

                ## Added to the bytes recieved:
                bytes_recieved=image
                if image:
                    # IF BYTES HAVE BEEN RECIEVED THEN...
                    while image:
                        image = connection.recv(4096)
                        length_recieved+=len(image)
                        #print(f"Length of Recieved Bytes {length_recieved}")
                        bytes_recieved+=image
                    else:
                        print(f"Final Length:{length_recieved}")
                        break
                            
                        #current_length+=len(str(image,FORMAT))
                        #with open ("WOW2.jpg", "rb") as image2string:
                        #base64_encoded_data = base64.b64encode(image)
                        #str_data = base64_encoded_data.decode(FORMAT)
                        #string = str(binary_data, FORMAT)
                        #str_len_bytes = len(str_data)
                        # if current_length < int(str_len_img):
                        #     # If the length of the bytes is less than the 
                        #     ## Known length it should be...
                        #     ## then it is known that we will needto 
                        #     continue
                        # elif current_length >= int(str_len_img):
                        #     #flyimg.close
                        #     break
                    # Ending with the null byte to signify the end of the file
                    ## Wrote this to the file in order to finalize this...
                    #flyimg.write(b'\x00')
            flyimg.write(bytes_recieved)
            flyimg.close()
            end = time.perf_counter_ns()
            print(f"Time for Single Image: {end-start} ns")
            break
            ## NOW IF WE WANT TO BREAK OUT OF HERE USER NEEDS TO TYPE
            ## BREAK
            # usr_status = input()
            # if usr_status == 'BREAK':
            #     break
            # else:
            #     continue


                    #flyimg.close
               # new_image.close
            # single_image(connection)
        elif test == 2:
            print("MEh")

        # NEED TO BASICALLY CLOSE THE CONNECTION...
    # print(CLIENTS)
    # for client in CLIENTS:
    #     print(client)
    #     thread =  threading.Thread(target=single_image)
    #     thread.start()
    #     thread.join()

def listener_single():
    """
    Listener function fora single thread

    Need to use this in testing...

    """
    print("Listening...")
    server.listen()
    # The conn and addr for the client in question
    while True:
        print("In Loop")
        conn, addr =  server.accept()
        print("listening...")
        #conn.send(bytes("Bye", FORMAT))
        thread =  threading.Thread(target=thread_manager, args=[conn, addr])
        thread.start()
        thread.join
        print(f"Client {conn,addr}")

    #     thread =  threading.Thread(target=handle_client, args=(conn,addr))
    #     print(thread)
    #     total_clients[thread] = client
    # # start the threads
    # for thread in total_clients:
    #     thread.start()
    #     thread.join()


# def run(func, args):
#     """
#     This function will basically input the names of functions and their arguments
#     into the thread.

#     This means that the threads can be run multiple times possibly for different processes...
#     """
#     # The number of connections that need to be made is X
#     ## So need to continue to listen for clients









    # """
    # Fuction that will allow the server to start listening for connections 

    # And then pass connections to handle_client which will run in a new thread..

    # HANDLES NEW CONNECTIONS

    # """

    # threads_init = threading.activeCount()
    # print("Initial number of threads: {threads_init}")
    # threads = threads_init - 1
    # tot_threads = 2
    # total_clients = np.empty(tot_threads)
    # for client in range(len(total_clients):
    #     print("Searching for Clients...")
    #     # when new connection occurs this will be stored in this object here..
    #     ## stores port and IP address of connection
    #     conn, addr =  server.accept()
    #     thread =  threading.Thread(target=handle_client, args=(conn,addr))
    #     print(thread)
    #     total_clients[thread] = client
    # # start the threads
    # for thread in total_clients:
    #     thread.start()
    #     thread.join()

    # server.listen()
    # print("Server is listening on {SERVER} for new connections")
    # while True:
    #     # when new connection occurs this will be stored in this object here..
    #     ## stores port and IP address of connection
    #     conn, addr =  server.accept()
    #     # made a new thread for running the handle client function to handle each individual client..
    #     ## target -> what function
    #     ## args -> What is inputted into the function...
    #     thread =  threading.Thread(target=handle_client, args=(conn,addr))
    #     # start the thread
    #     thread.start()
    #     print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}") # how many threads are active in this process... new thread per client... but we do start with one iniital thread which is the listening thread for new connections



print("Starting Server")
listener_single()

