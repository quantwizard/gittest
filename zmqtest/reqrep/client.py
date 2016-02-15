#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
import sys
from time import sleep

port = "5555"
if len(sys.argv) > 1:
    port = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

while True:
    sleep(5)
    socket.send("here is msg from client")
    msg = socket.recv()
    print "Received message(%s) from server." % msg
