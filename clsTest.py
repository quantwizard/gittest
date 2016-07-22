from time import sleep


class SyncManager(object):
    """
    This class is singleton, and is used to sync files.
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SyncManager, cls).__new__(cls, *args, **kwargs)
            # notice that if you want to use args, you need args in __init__
            cls.name = args[0]
            print "new instance"
        return cls._instance
    def __init__(self, name):
        pass

    def printit(self):
        print self.name[0]
        print self._instance

    @classmethod
    def printname(cls):
        print cls.name

    @classmethod
    def close(cls):
        print "name is: %s" % cls.name
        del cls._instance

def main():

    sm1 = SyncManager("Jack")
    sm2 = SyncManager("Jim")
    print "sm1.name: %s" % sm1.name
    print "sm2.name: %s" % sm2.name
    sm1.close()
    # SyncManager.close()
    sm3 = SyncManager("Elon")
    print "sm3.name: %s" % sm3.name
    sm3.printit()
    sm3.printname()
    while 1:
        print "..."
        sleep(2)

if __name__ == '__main__':
    main()