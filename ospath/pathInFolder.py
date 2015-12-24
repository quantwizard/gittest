import os


def getFilePath(filename):
    dirname = os.path.dirname(__file__)
    print dirname
    if os.path.exists(os.path.join(dirname, filename)):
        print "the file exists"
    else:
        print "not exists"