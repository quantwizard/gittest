class Singleton(object):

    # def __new__(cls, *args, **kwargs):
    #     if not "_instance" in vars(cls):
    #         cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    #     return cls._instance

    # also this is ok

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def main():
    a = Singleton()
    b = Singleton()
    if a is b:
        print "a is b"
    print a
    print b

if __name__ == '__main__':
    main()
