#!/usr/bin/env python3

# THREADING TESTING 
"""

This script will test out the functionality of threading

Will simulate 6 different pis... then will move up to 10


Will be running CONCURRENTLY....

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