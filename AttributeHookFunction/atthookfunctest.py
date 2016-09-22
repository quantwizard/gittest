class AttHookFuncTest(object):
    def __init__(self):
        self.exist = 5

    def __getattr__(self, name):
        print "__getattr__ is called for %s" % name
        setattr(self, name, 7)
        return 7

    # def __getattribute__(self, name):
    #     print "__getattribute__ is called for %s" % name

    def __setattr__(self, name, value):
        print "__setattr__ is called for %s" % name
        super(AttHookFuncTest, self).__setattr__(name, value)


def main():
    testObj = AttHookFuncTest()
    testObj.pro1 = 9
    print testObj.pro1
    print "------"
    print testObj.pro2
    print "------"
    print testObj.exist


if __name__ == '__main__':
    main()