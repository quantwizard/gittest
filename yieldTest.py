from itertools import chain

def testy(x, y):
    for i in xrange(x):
        j = yield str(i)
        print "i is %d" % i
	print "j is %s" % str(j)
    for n in xrange(y):
        yield str(n)
        print n

def testy2(x, y):
    for item in xrange(x):
        yield item, item + y

def main():
    results = [x for x in testy(5, 8)]
    print results
    # print list(set(list(testy(5, 8))))
    # for i in testy2(3, 5):
    #     print i
    # print list(chain.from_iterable(testy2(3, 5)))
    # print testy2(0,0).next()

if __name__ == "__main__":
    main()
