#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
import sys
from time import sleep


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc:///tmp/feed/0")

while True:

    msg = socket.recv()
    socket.send("I'm msg from server")
    print "Received message(%s) from client." % msg
