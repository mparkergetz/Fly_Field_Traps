#!/usr/bin/env python3
import threading
import numpy as np
import time 

start = time.perf_counter()

def connection()
	return print("Hi")

def send_start_time():

def convert_image():
	"""
	Converts image from jpg or png into byte format
	"""
	vals = np.random.randint(low_num,high_num)
	return print(f"Random integers {vals}")

def send_image():
	"""
	This function will send an image 
	"""
# NEED THE FUNCTIONS TO SEND VERY VERY SIMPLE STRING MESSAGES TO THE CLIENTS...
## THE CLIENTS WILL NEED TO BE THE ONES TO SEND SOME MORE COMPLICATED STRINGS THAT WILL NEED TO BE PROCESSED...



Threads = []
num_threads = 2
# First Start By Starting the Threads and Appending Them
for t in range(num_threads):
	thread_new =  threading.Thread(target=rando, args=(int(input()),int(input())))
	thread_new.start()
	thread_new.join()
	Threads.append(thread_new)

# Start and Join...

	# thread_new =  threading.Thread(target=check)
	# thread_new.start()
	# thread_new.join()
	# Threads.append(thread_new)
	
	

finish = time.perf_counter()
print(f"Time: {finish-start}")
# thread =  threading.Thread(target=handle_client, args=(conn,addr))
# start the thread
# 