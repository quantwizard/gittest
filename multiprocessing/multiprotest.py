from multiprocessing import Pool
from time import sleep
from sys import stdout


def f(x):
    sleep(3)
    print "already 3s"
    stdout.flush()
    sleep(10)
    print "function f is over"
    stdout.flush()
    # return result
    return "errorcode:%d:test msg." % x

def main():
    # if we don't set processes, it will use None, that means
    # it will use multiprocessing.cpu_count() as the process number
    # also there are initializer, initargs and maxtasksperchild parameters
    # if we provide initializer function, then each work process will call it
    pool = Pool(processes=2)

    # use apply_async, it will run async without blocking the main process
    results = [pool.apply_async(f, args=(x,)) for x in range(10)]
    print "launch is over"

    # we can use get method to get the result
    # if timeout, will raise TimeoutError
    print [res.get(timeout=1) for res in results]


def proresult(result):
    print result


def main2():
    # here I set processes=2, so each time only 2 f can be executed
    # even when f is sleeping, it will wait until the f is over.
    pool = Pool(processes=2)

    # when each process result is ready, the callback function will be called
    [pool.apply_async(f, args=(x,), callback=proresult) for x in range(10)]
    print "launch is over"
    stdout.flush()
    # donot accept new tasks after close
    pool.close()

    # block until task is over or terminate.
    # notice: join() have to be called after close() or terminate()
    pool.join()
    print "main2 is over"
    stdout.flush()


def main3():
    pool = Pool(processes=4)
    results = [pool.apply_async(f, args=(x,), callback=proresult) for x in range(5)]
    print "launch is over"

    # donot accept new tasks after close
    pool.close()
    sleep(5)

    # terminate all processes in the pool immediately
    pool.terminate()

    # block until task is over or terminate.
    pool.join()
    print "main3 is over"

if __name__ == '__main__':
    # main()
    main2()