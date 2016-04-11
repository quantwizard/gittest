#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016-2017
# Author: Liu Feng
import socket

EOL1 = b"\n\n"
EOL2 = b"\n\r\n"
response = b"HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n"
response += b"Content-Type: text/plain\r\nContent-Length: 12\r\n\r\n"
response += b"hello, world"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 5555))
serversocket.listen(5)

clientsocket, address = serversocket.accept()
request = b""
while EOL1 not in request and EOL2 not in request:
    request += clientsocket.recv(1024)
print request.decode()
clientsocket.send(response)
clientsocket.close()

serversocket.close()
