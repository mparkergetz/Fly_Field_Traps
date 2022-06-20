#!/usr/bin/env python3
# 6/15/2022 USE THIS VERSION!
import socket
import threading

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

#SERVER FOR THE UBUNTU MACHINE
SERVER = '192.168.220.91'
#print(SERVER)
# ADDR: address that we will use to bind to the socket
ADDR = (SERVER, PORT)

FORMAT = 'utf-8'

# disconnect message
## when we recieve this message close client from server...
DISCONNECT_MESSAGE = "!Disconnect"
# Type of socket utilized for the server...
## Over internet.... -> Switch this method maybe?
## 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV6 addresses..., Steaming Data 

# bind socket to the address....
server.bind(ADDR)

def handle_client(conn,addr):
    """
    handles communication between the client and the server

    INDIVIDUAL CLIENT AND SERVER...


    also deals with disconnection and reconnection... so reconnection it knows the client left...
    """

    print(f"[New CONNECTION {addr} connected")
    connected = True
    while connected:
        # message protocols need to figur eout...
        ## will not run this code until a message is recieved from client..
        ## how many bytes to recieve from client... using header...
        # 1st message will be a message of length 64...will have number that will have length of number of bytes of what we are about to recieve.
        ### then decode since encoded in byte format.. so decode from byte to string...
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        # Need to check to see if the message is a valid message..
        ## since when we connect we don't get a valid message its basically blank

        if msg_length:
            # string to int..
            msg_length = int(msg_length)
            # now determine the number of byts we are recieveing for the actual message
            msg= conn.recv(HEADER).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                print(f"[{addr}]{msg}")
                connected = False
            print(f"[{addr}]{msg}")
    conn.close()




def start():
    """
    Fuction that will allow the server to start listening for connections 

    And then pass connections to handle_client which will run in a new thread..

    HANDLES NEW CONNECTIONS

    """
    server.listen()
    print(f"[SERVER] LISTENING on {SERVER}")
    while True:
        # when new connection occurs this will be stored in this object here..
        ## stores port and IP address of connection
        conn, addr =  server.accept()
        # made a new thread for running the handle client function to handle each individual client..
        ## target -> what function
        ## args -> What is inputted into the function...
        thread =  threading.Thread(target=handle_client, args=(conn,addr))
        # start the thread
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}") # how many threads are active in this process... new thread per client... but we do start with one iniital thread which is the listening thread for new connections



print("Starting Server")
start()

