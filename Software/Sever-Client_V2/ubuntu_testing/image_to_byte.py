# THIS SEEMS TO BE A TEMPORARY IMAGE TO BYTE SOLUTION!

import base64
import sys

with open ("fly.jpg", "rb") as image2string:
	converted_string = base64.b64encode(image2string.read())

user_input = input()
if user_input == "Yes":
	## Then make it back into an image
	# file = open('encode.bin', 'rb')
	# byte =file.read()
	# file.close()
	new_image = open("WOW.jpg", 'wb')
	new_image.write(base64.b64decode((converted_string)))
	new_image.close



