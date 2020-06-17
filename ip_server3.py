#!/usr/bin/env python3

"""
https://realpython.com/python-sockets/
https://blog.myhro.info/2017/01/how-fast-are-unix-domain-sockets

"""

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print('Server ready to receive.')
    '''
    temp move accept to allow repeated client loop connections and remove close
    not good practice? but used to test performance in non echo/ping scenario
    '''
    # conn, addr = s.accept()

    # with conn:
    #    print('Connected by', addr)
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
        #conn.close()
