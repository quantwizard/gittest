import inspect


def add(x, y):
    f = inspect.currentframe()
    print f.f_locals
    print f.f_back
    # print inspect.stack()
    print inspect.stack()[1][3]
    # tb = sys.exc_info()
    return x + y

def test():
    add(1, 2)


if __name__ == '__main__':
    test()