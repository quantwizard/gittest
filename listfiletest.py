import time

path = "/root/test_report_server/templates/*.html"
start = time.time()
import glob
file_list = glob.glob(path)
end = time.time()
print "glob time: %f" % (end-start)
start = time.time()
from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
end = time.time()
print "listdir time: %f" % (end-start)