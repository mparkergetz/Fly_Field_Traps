#!/usr/bin/env python3
"""

Need to have multiple threads or utilize multiprocessing
in order to send messages back and forth

There will need to at least be a thread of each pi

"""
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '' 
port = 20
s.bind((host, port)) 
s.listen(5)
print("Waiting for connections") 
while True: 
    c, addr = s.accept() 
    print('Got connection from', addr) 
    c.send(b'Thank you for connecting') 
    c.close()