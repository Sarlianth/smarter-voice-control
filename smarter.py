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