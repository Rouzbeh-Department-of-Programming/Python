#!/usr/bin/env python
import socket
import sys
TCP_IP = sys.argv[1]
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print("Server IP Address", TCP_IP)
print("Server Port Address", TCP_PORT)
s.listen(1)
print("Server Is Listening")
conn, addr = s.accept()
while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
                break
        print("received data from client:", data)
        conn.send(data)  # echo
conn.close()

