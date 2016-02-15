#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016
# Author: Liu Feng

import zmq
import sys
import ast


def main(port=None):
    port = "5555"
    if port:
        port = port
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.connect('tcp://localhost:%s' % port)
    topic_filter1 = "888"
    topic_filter2 = "899"
    sub.setsockopt(zmq.SUBSCRIBE, topic_filter1)
    sub.setsockopt(zmq.SUBSCRIBE, topic_filter2)
    while True:
        topic, content = sub.recv_multipart()
        print "receive topic: content<%s: %s>" % (topic, content)
        con = ast.literal_eval(content)
        print "the value is: %d" % con['value']

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
