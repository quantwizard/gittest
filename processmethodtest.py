from multiprocessing import Process
from time import sleep
import signal


def f(name):
    print 'hello', name
    sleep(15)


def onsigchld(a, b):
    print 'receive child signal'


if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, onsigchld)
    p = Process(target=f, args=('bob',))
    p.start()
    sleep(2)
    y = p.terminate()

    print y
    print type(y)

