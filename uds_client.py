#!/usr/bin/env python3

"""
https://realpython.com/python-sockets/
https://blog.myhro.info/2017/01/how-fast-are-unix-domain-sockets
"""

import socket
import time

server_addr = '/tmp/uds_server.sock'
duration = 1
end = time.time() + duration
msgs = 0

print('Sending messages...')

while time.time() < end:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(server_addr)
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        msgs += 1
        s.close()

print('Receiving message', repr(data))
print(data.decode("utf-8"))
print('Received {} messages in {} second(s).'.format(msgs, duration))
