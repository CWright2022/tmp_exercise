# /tmp/ Covert Channel
by Cayden Wright, for Covert Comms Fall 2025 (Daryl Johnson)

## Description
This repo implements a covert communication channel that uses file sizes within the /tmp/ directory to communicate via two processes that aren't usually able to communicate.

## `sender.py`
`sender.py` will send a message of your choosing (defined by the `DATA_TO_SEND` variable) by writing a file to the /tmp/ directory with a specific length. After the text is converted to binary, the following occurs:
 - To send a `0`, the file length is set to a random value  1-99 bytes (inclusive)
 - To send a `1`, the file length is set to a random value 100-200 bytes (inclusive)
 - To signal end of transmission, the file length is set to a random value 200-300 bytes.
 - To send a message, simply set `DATA_TO_SEND` to your message and run the program without any arguments.
 -  ```python3 sender.py```

## `receiver.py`
`receiver` will recieve a message sent by `sender.py` by reading the file length of `/tmp/data` according to the above rules. It will convert this binary back to text and print it to the terminal
 - To recieve a message, simply run the program without any arguments.
 - ```python3 receiver.py```