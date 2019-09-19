#!/usr/bin/python3

import socket

with socket.socket() as s:
    s.bind(('localhost', 8000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

