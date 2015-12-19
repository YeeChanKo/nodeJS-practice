#! /usr/bin/env python
import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    print 'connection from', address
    data = client.recv(size)
    response = '<html><body><H1>Hello Pi</H1></body></html>
    if data:
        client.send(response)
    client.close()