from multiprocessing import Process
from time import sleep
import signal
import os


def f(name):
    print "this is subprocess:"
    print "subprocess pid is %d" % os.getpid()
    print "subprocess group id is %d" % os.getpgrp()
    sleep(115)


if __name__ == '__main__':
    # print os.getegid()
    # print os.getgroups()
    # print os.getgid()
    gid = os.getpgrp()
    print "process groupid is %d" % gid
    # signal.signal(signal.SIGCHLD, onsigchld)
    p = Process(target=f, args=('bob',))
    p.start()
    sleep(5)
    print "killing...."
    # os.killpg(gid, signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGTERM)
