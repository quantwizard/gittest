#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016-2017
# Author: Liu Feng
import socket
import select

EOL1 = b"\n\n"
EOL2 = b"\n\r\n"
response = b"HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n"
response += b"Content-Type: text/plain\r\nContent-Length: 12\r\n\r\n"
response += b"hello, world"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("123.56.9.190", 5555))
serversocket.listen(5)
serversocket.setblocking(0)

# create epoll
epoll = select.epoll()

# register what socket you want to monitor, wrap epoll_ctl
# events可以是以下几个宏的集合：
# EPOLLIN ：表示对应的文件描述符可以读（包括对端SOCKET正常关闭）；
# EPOLLOUT：表示对应的文件描述符可以写；
# EPOLLPRI：表示对应的文件描述符有紧急的数据可读（这里应该表示有带外数据到来）；
# EPOLLERR：表示对应的文件描述符发生错误；
# EPOLLHUP：表示对应的文件描述符被挂断；
# EPOLLET： 将EPOLL设为边缘触发(Edge Triggered)模式，这是相对于水平触发(Level Triggered)来说的。
# EPOLLONESHOT：只监听一次事件，当监听完这次事件之后，如果还需要继续监听这个socket的话，
#               需要再次把这个socket加入到EPOLL队列里
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    connections = {}; requests = {}; responses = {}
    while True:
        # Query the epoll object to find out if any events of interest may have occurred. 
        # The parameter "1" signifies that we are willing to wait up to one second for such an
        # event to occur. If any events of interest occurred prior to this query, 
        # the query will return immediately with a list of those events.
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                clientsocket, addr = serversocket.accept()
                clientsocket.setblocking(0)
                epoll.register(clientsocket.fileno(), select.EPOLLIN)
                connections[clientsocket.fileno()] = clientsocket
                requests[clientsocket.fileno()] = b""
                responses[clientsocket.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                # Once the complete request has been received, then unregister
                # interest in read events and register interest in write
                # (EPOLLOUT) events. Write events will occur when it is possible
                # to send response data back to the client.
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT)
                    print '-'*40 + '\n' + requests[fileno].decode()
            elif event & select.EPOLLOUT:
                # Send the response data a bit at a time until the
                # complete response has been delivered to the operating system
                # for transmission.
                # 说明每次send不一定能把response中所有数据都发送，可能只发送了一部分
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    # Once the complete response has been sent,
                    # disable interest in further read or write events.
                    epoll.modify(fileno, 0)
                    # A socket shutdown is optional if a connection is
                    # closed explicitly. This example program uses it in order to
                    # cause the client to shutdown first. The shutdown call
                    # informs the client socket that no more data should be sent
                    # or received and will cause a well-behaved client to close the
                    # socket connection from it's end.
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            # The HUP (hang-up) event indicates that the client socket has been
            # disconnected (i.e. closed), so this end is closed as well.
            # There is no need to register interest in HUP events.
            # They are always indicated on sockets that are registered with
            # the epoll object.
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
