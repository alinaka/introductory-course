#!/usr/bin/python3

try:
    file = open('io_basics.md')
    print(f"file descriptor is {file.fileno()}")
    file.close()
    file = open('os_basics.md')
    print(f"file descriptor is {file.fileno()}")
finally:
    file.close()
