#!/usr/bin/env python
# -*- coding: utf-8 -*-
#imports
import sys
import socket
import json
import binascii

#defining method names
METHOD_BREW = "brew"
METHOD_RESET = "reset"
api_method = " "
msg = " "
message_to_send = ""
success = ""
message = ""

#ip address and port number to connect to coffee maker
TCP_IP = '172.16.1.91'
TCP_PORT = 2081
BUFFER_SIZE = 10

if api_method == METHOD_BREW:
	message_to_send = "7"

elif api_method == METHOD_RESET:
	message_to_send = "\x10"

#connect to machine and send message_to_send
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send( bytearray(message_to_send, 'utf8') )
	data = s.recv(BUFFER_SIZE)
	s.close()
except (socket.error, msg):
	print ('Failed. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit();

print (data)
#translate to unicode
#return_code = unicode(data)

print (json.dumps({'success': success, 'message': message, 'return_code': repr(data)[1:10]}))

quit()
sys.exit()