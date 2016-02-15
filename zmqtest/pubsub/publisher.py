#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
import sys
from time import sleep
from random import randint

def main(port=None):
    port = "5555"
    if port:
        port = port
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:%s' % port)
    while True:
        sleep(5)
        topic = randint(888, 900)
        content = {"a": 1, "value": topic}
        print "topic:content(%d:%s)" % (topic, str(content))
        publisher.send_multipart(['%03d' % topic, str(content)])



class Content(object):
    def __init__(self, value):
        self.value = value

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
