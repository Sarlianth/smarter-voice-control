#!/usr/bin/env python

#imports
import sys
import socket
import json

#defining method names
METHOD_BREW = "brew"
METHOD_RESET = "reset"

#ip address and port number to connect to coffee maker
TCP_IP = '192.168.1.192'
TCP_PORT = 2081
BUFFER_SIZE = 10

if api_method == METHOD_BREW:
	message_to_send = "7"
elseif api_method == METHOD_RESET
	message_to_send = "\x10"

#connect to machine and send message_to_send
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(message_to_send)
	data = s.recv(BUFFER_SIZE)
	s.close()
except socket.error, msg:
	print 'Failed. Error code: ' + str(msg[0]) + ', Message : ' + msg[1]
	sys.exit()

#translate to unicode
return_code = unicode(data)

print json.dumps({'success': success, 'message': message, 'return_code': repr(data)[1:10]})

quit()
sys.exit()