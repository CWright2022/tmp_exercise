#!/usr/env/python3
#Cayden Wright - 9/10/2025
#Covert Comms with Daryl Johnson
#Fall 2025
import os
import random

DATA_TO_SEND = "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. - John 3:16"
    
def wait_for_rx_consume():
    """
    waits for the reciever to delete /tmp/dsr, indicating it has consumed the data
    """
    while os.path.exists("/tmp/dsr"):
        pass
def set_dsr():
    """
    tells rx we are ready for them to read the data
    """
    with open("/tmp/dsr", "w") as f:
                f.write("")
def main():
    #convert message to binary
    binary = ''.join(format(byte, '08b') for byte in DATA_TO_SEND.encode('utf-8'))
    print(f"MESSAGE: {DATA_TO_SEND}")
    print(f"BINARY: {binary}")
    #signal receiver we are ready, wait for response
    #send data
    i = 0
    for bit in binary:
        #if 1, write 100-200 bytes, if 0 write 1-99 bytes
        if bit == '1':
            with open("/tmp/data", "w") as f:
                bytes = random.randint(100,200)
                f.write(os.urandom(bytes).hex())
                # print(f"wrote {bytes} bytes to /tmp/data")
        elif bit == '0':
            with open("/tmp/data", "w") as f:
                bytes = random.randint(1,99)
                f.write(os.urandom(bytes).hex())
                # print(f"wrote {bytes} bytes to /tmp/data")
        print(f"sent bit {bit} ({i+1}/{len(binary)})")
        # print(f"/tmp/data size: {os.path.getsize('/tmp/data')}")
        i+=1
        set_dsr()
        #wait for receiver to consume data (it will delete /tmp/data))
        wait_for_rx_consume()
    #after we're done, write >200 bytes to signal end of transmission
    with open("/tmp/data", "w") as f:
        bytes = random.randint(201,300)
        f.write(os.urandom(bytes).hex())
        # print(f"wrote {bytes} bytes to /tmp/data")
        # print(f"/tmp/data size: {os.path.getsize('/tmp/data')}")
    set_dsr()
    print("transmission complete")
    

if __name__ == "__main__":
    main()
    