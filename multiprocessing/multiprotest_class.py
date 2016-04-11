from multiprocessing import Pool
from time import sleep
from sys import stdout
import functools

class PoolTest(object):
    def __init__(self):
        self.a = "111"
    def foo(self, x):
        sleep(10)
        self.a = "%d" % x
        print self.a
        stdout.flush()
        return "result is %d" % x

def proresult(result):
        print result

def covmethod(obj, x):
    return obj.foo(x)

def main():
    pool = Pool(processes=4)

    p = PoolTest()
    newfunc = functools.partial(covmethod, p)
    # when each process result is ready, the callback function will be called
    [pool.apply_async(newfunc, args=(x,), callback=proresult) for x in range(10)]
    print "launch is over"
    stdout.flush()
    # donot accept new tasks after close
    pool.close()

    # block until task is over or terminate.
    # notice: join() have to be called after close() or terminate()
    pool.join()
    print "main is over"
    stdout.flush()

if __name__ == '__main__':
    main()