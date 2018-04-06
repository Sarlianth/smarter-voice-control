#!/usr/bin/env python
import sys
import socket
import json

#method names
API_METHOD_BREW = "brew"
API_METHOD_RESET = "reset"
API_METHOD_GRIND = "set_grind"
API_METHOD_CUPS = "cups"

return_code = ""

#IP address of the smarter
TCP_IP = '172.16.1.91'
TCP_PORT = 2081
BUFFER_SIZE = 10

#default method to call
api_method = sys.argv[1]

if api_method == API_METHOD_BREW:
	message_to_send = "7"
elif api_method == API_METHOD_RESET:
	message_to_send = "\x10"
elif api_method == API_METHOD_GRIND:
	message_to_send = "\x3c\x7e"
elif api_method == API_METHOD_CUPS:
	n = input("How many cups? ")

	if n == 1:
		message_to_send = "\x36\01\x7e"
	elif n == 2:
		message_to_send = "\x36\02\x7e"
	elif n == 3:
		message_to_send = "\x36\03\x7e"
	elif n == 4:
		message_to_send = "\x36\04\x7e"
	elif n == 5:
		message_to_send = "\x36\05\x7e"
	elif n == 6:
		message_to_send = "\x36\06\x7e"
	elif n == 7:
		message_to_send = "\x36\07\x7e"
	elif n == 8:
		message_to_send = "\x36\08\x7e"
	elif n == 9:
		message_to_send = "\x36\09\x7e"
	elif n == 10:
		message_to_send = "\x36\10\x7e"
	elif n == 11:
		message_to_send = "\x36\11\x7e"
	elif n == 12:
		message_to_send = "\x36\12\x7e"
	else:
		message_to_send = "\x36\02\x7e"
		print("Maximum of 12 cups!")
	
	print(message_to_send)

#connection to machine
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(str.encode(message_to_send))
	#s.send(message_to_send)
	data = s.recv(BUFFER_SIZE)
	s.close()
except (socket.error, msg):
	print ('Failed. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit();

#convert response from machine to unicode
return_code = str(data, 'utf-8')

#default values
success=0
message=""

print (return_code)

#find out what the machine response means (not working well)
if return_code =="\x03\x00~":
	success=1
	message="brewing"
elif return_code=="\x03\x01~":
	message="already brewing"
elif return_code=="\x03\x05~":
	message="no carafe"
elif return_code=="\x03\x06~":
	message="no water"
elif return_code=="\x03i~":
	success=1
	message="reset"
else:
	message="check machine"

#ouput JSON
print (json.dumps({'success': success,'message':message,'return_code':repr(data)[1:10]}))

quit()
sys.exit()