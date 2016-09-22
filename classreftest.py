

class Test1(object):
    def __init__(self):
        print "this is Test1"


class Test2(object):
    def __init__(self):
        print "this is Test2"


class Test3(object):
    def __init__(self):
        print "this is Test3"

test_class = {"a": Test1,
              "b": Test2,
              "c": Test3}

def main():
    j = {"jj": "a"}
    test1 = test_class.get(j['jj'])()


if __name__ == '__main__':
    main()