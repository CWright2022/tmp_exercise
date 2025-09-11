#!/usr/env/python3
#Cayden Wright - 9/10/2025
#Covert Comms with Daryl Johnson
#Fall 2025
import os

def binary_to_text(binary_str: str) -> str:
    """
    converts raw data we got from /tmp/data back to text
    """
    data_bytes = bytes(
        int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)
    )
    return data_bytes.decode("utf-8")

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
            print("got stop signal")
            break
        #if size 100-200, bit is 1, if size 1-99, bit is 0
        elif size >= 100:
            data += '1'
            print(f"received bit 1 (size={size})")
        elif size < 100:
            data += '0'
            print(f"received bit 0 (size={size})")
        #delete /tmp/data and /tmp/dsr to signal we have consumed the data
        # os.remove("/tmp/data")
        os.remove("/tmp/dsr")
        # input("press enter to continue...")
    #convert binary to string
    print(f"RAW BINARY: {data}")
    message = binary_to_text(data)
    print(f"MESSAGE: {message}")
    

if __name__ == "__main__":
    main()
    