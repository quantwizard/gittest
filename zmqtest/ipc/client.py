#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
from time import sleep


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("ipc:///tmp/feed/0")

while True:
    sleep(5)
    socket.send("here is msg from client")
    msg = socket.recv()
    print "Received message(%s) from server." % msg
