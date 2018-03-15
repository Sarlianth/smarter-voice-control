#!/usr/bin/env python
import sys
import socket
import json

#method names
API_METHOD_BREW = "brew"
API_METHOD_RESET = "reset"
API_METHOD_GRIND = "set_grind"

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