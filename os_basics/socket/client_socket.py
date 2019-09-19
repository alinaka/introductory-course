#!/usr/bin/python3

import socket

with socket.socket() as s:
    s.connect(('localhost', 8000))
    s.sendall(b'Hello there')
    data = s.recv(1024)
print(data.decode())
