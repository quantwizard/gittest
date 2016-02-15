#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng
'''
socket zmq.REQ will block on send unless it has successfully received a reply back.
socket zmq.REP will block on recv unless it has received a request.
'''
import zmq
import sys

port = "5555"
if len(sys.argv) > 1:
    port = sys.argv[1]

context = zmq.Context()
# server use zmq.REP type
socket = context.socket(zmq.REP)
socket.bind('tcp://*:%s' % port)

while True:
    # wait for next request from client
    msg = socket.recv()
    print "receive message(%s) from client" % msg
    socket.send('Received your message, please go on.')