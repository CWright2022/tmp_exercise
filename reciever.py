#!/usr/env/python3
#Cayden Wright - 9/10/2025
#Covert Comms with Daryl Johnson
#Fall 2025
import os
import random

def main():
    print("waiting for transmission...")
    data = ""
    while True:
        #wait for /tmp/dsr to exist
        while not os.path.exists("/tmp/dsr"):
            pass
        #read /tmp/data size
        size = os.path.getsize("/tmp/data")/2
        print(f"data size: {size}")
        #if size > 200, end of transmission
        if size > 200:
            print("transmission complete")
            break
        #if size 100-200, bit is 1, if size 1-99, bit is 0
        elif size >= 100:
            data += '1'
            print(f"received bit 1 ({len(data)})")
        elif size < 100:
            data += '0'
            print(f"received bit 0 ({len(data)})")
        #delete /tmp/data and /tmp/dsr to signal we have consumed the data
        # os.remove("/tmp/data")
        os.remove("/tmp/dsr")
        # input("press enter to continue...")
    #convert binary to string
    message = ''.join(chr(int(b, 2)) for b in data.split(' '))
    print(f"received message: {message}")
    

if __name__ == "__main__":
    main()
    