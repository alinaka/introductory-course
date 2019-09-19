#!/usr/bin/python3

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(f"started {self.getName()}")
        time.sleep(1)
        print(f"finished {self.getName()}")

def main():
    for i in range(5):
        t = MyThread()
        t.start()
        time.sleep(.9)

if __name__ == "__main__":
    main()

