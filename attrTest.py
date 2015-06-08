class attrTest:
    count = 0
    digit = 0
    def __init__(self, number):
        self.number = number
        self.count += 1
        self.__class__.digit += 1

class subTest(attrTest):
    def __init__(self):
        attrTest.__init__(self,5)
        print self.number

if __name__ == "__main__":
    print "attrTest count is %s" % attrTest.count
    ins = attrTest(2)
    ins2 = attrTest(3)
    print "ins number is %d" % ins.number
    print "ins2 number is %d" % ins2.number
    print "ins count is %d" % ins.count
    print "ins2 count is %d" % ins2.count
    print "ins digit is %d" % ins.digit
    print "ins2 digit is %d" % ins2.digit
    subins = subTest()
