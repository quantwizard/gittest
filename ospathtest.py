import os
from ospath.pathInFolder import getFilePath
if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../', 'hello.c')
    if os.path.exists(filename):
        print "file exists"
    else:
        print "file doesn't exists"

    getFilePath("userdict.py")