#!/usr/bin/env python
import socket
import time
import sys

TCP_IP = sys.argv[1]
TCP_PORT = 8000
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("Connected to server...")
while True:
		MESSAGE = input()
		s.send(MESSAGE.encode())
		data = s.recv(BUFFER_SIZE)
		print("received data from server:", data)
s.close()
