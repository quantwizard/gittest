import threading


class ExceptionThreadTest(threading.Thread):
    def __init__(self):
        super(ExceptionThreadTest, self).__init__()
        self.setName("testexceptionthread")

    def run(self):
        print "Thread begin to run."
        raise Exception("this is exception test\n")
        print "after exception"


class ExceptionThreadTest2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._exc = None
        self.setName("testexceptionthread2")

    def run(self):
        try:
            print "Thread begin to run."
            raise Exception("this is exception test\n")
            print "after exception"

        except Exception, e:
            import sys
            self._exc = sys.exc_info()
            print self._exc

    def join(self):
        threading.Thread.join(self)
        if self._exc:
            msg = "Thread %s threw an exception: %s" % (self.getName(),
                                                        self._exc[1])
            new_exc = Exception(msg)
            raise new_exc.__class__, new_exc, self._exc[2]


def main():
    try:
        t = ExceptionThreadTest2()
        print t.__class__
        t.start()
        t.join()
        print "after thread"
    except Exception, e:
        print "caught exception: %s" % e


if __name__ == '__main__':
    main()
