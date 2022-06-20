#!/usr/bin/env python3

# THREADING TESTING on UBUNTU....
"""

This script will test out the functionality of threading

Will simulate 6 different pis... then will move up to 10


Will be running CONCURRENTLY....

THREADING IS APPROPRIATE FOR COMMUNICATION BETWEEN DEVICES...
 THIS WAY A THREAD CAN HAVE THE IP ADDRESSED SAVED SO A SPECIFCA THREAD CAN BE ACCESSED
 
 
ADDITIONALLY ALL OF THE THREADS CAN BE RUN 
Concurrently for when they will start with only a slight delay in between



..


"""

import threading
import time

# start time..
start = time.perf_counter()

def do_something():
	print('Sleeping 1 second')
	time.sleep(1)
	print('Done Sleeping..')

do_something()
do_something()
finish =time.perf_counter()
print(f'Finished in {round(finish-start, 3)}second(s)')