#!/usr/bin/python3

import threading

c = 0

def inc(i):
    global c
    print(f"{i} here")
    for i in range(1000000):
        c += 1
    print(f"leaving {i}")

t1 = threading.Thread(target=inc, args=(1,))
t2 = threading.Thread(target=inc, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(c)
