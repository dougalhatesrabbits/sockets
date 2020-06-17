#!/usr/bin/env python3

"""
https://realpython.com/python-sockets/
https://blog.myhro.info/2017/01/how-fast-are-unix-domain-sockets
"""

import socket
import time
import sys

#toolbar_width = 80

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
duration = 1
end = time.time() + duration
msgs = 0

print('Sending messages...')

'''
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['
'''
while time.time() < end:
    # for i in range(toolbar_width):
    #time.sleep(0.1)  # do real work here
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        msgs += 1
        s.close()
    '''
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

    if msgs % 80 == 0:
        sys.stdout.write("]\n[")  # this ends the progress bar
    '''

print('\nReceiving message', repr(data))
print(data.decode("utf-8"))
print('Received {} messages in {} second(s).'.format(msgs, duration))
