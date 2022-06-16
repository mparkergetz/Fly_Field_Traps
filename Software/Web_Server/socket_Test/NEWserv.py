#!/usr/bin/env python3
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