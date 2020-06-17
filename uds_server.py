#!/usr/bin/env python3

"""
https://realpython.com/python-sockets/
https://blog.myhro.info/2017/01/how-fast-are-unix-domain-sockets

"""
import os
import socket

server_addr = '/tmp/uds_server.sock'

if os.path.exists(server_addr):
    os.unlink(server_addr)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(server_addr)
    s.listen()
    print('Server ready to receive.')
    '''
    temp move accept to allow repeated client loop coonnections and remove close
    not good practice? but used to test performance in none echo/ping scenario
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
