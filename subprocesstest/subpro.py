def test():
    # return "111"
    # raise ErrorCode("400", "this is error code.")
    print "111:this is an error"

if __name__ == '__main__':
    test()


class ErrorCode(Exception):
    def __init__(self, code, msg):
        super(ErrorCode, self).__init__()
        self.code = code
        self.msg = msg

    def __str__(self):
        return "%s: %s" % (self.code, self.msg)
