#!/usr/bin/python3

import os

pipe = os.path.join(os.getcwd(), 'pipe')

with open(pipe) as f:
    while True:
        print(f.read(5))

