#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

'''
pair means both server and client can send data to peer continuously
compair to request/reply, server only send data when get request
'''
import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send("Server message to client3")
    msg = socket.recv()
    print msg
    time.sleep(1)