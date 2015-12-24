import crash_on_ipy


def funcA(par):
    now = par
    print now


def main():
    funcA("hello")
    mac = "hahaha"
    print "We will raise an exception"
    raise Exception("this is crash_on_ipy test")
    print "This is the end"


if __name__ == '__main__':
    main()
