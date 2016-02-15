#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    socket.send("client message to server1")
    msg = socket.recv()
    print msg
    time.sleep(1)