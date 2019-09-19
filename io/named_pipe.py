#!/usr/bin/python3

import os

pipe = os.path.join(os.getcwd(), 'pipe')

if not os.path.exists(pipe):
    os.mkfifo(pipe)

with open(pipe, 'w') as f:
    while True:
        f.write(input())
        f.flush()
