testfile = open(r"D:\BugReport.txt", "rb")
print "tell output %s" % testfile.tell()
'''
for i in testfile:
    print i
print "tell output %s" % testfile.tell()
print "seek to (-10, 2)"
testfile.seek(-10, 2)
data = testfile.read(5)
print "the data is %s" % data
print "tell output %s" % testfile.tell()
for i in testfile:
    print i

print "now tell again"
print "tell output %s" % testfile.tell()
'''
# data = testfile.read(5)
# print data
testfile.seek(5)
print "tell output %s" % testfile.tell() 

# writefile = open(r"D:\program\python\test2.txt", "wb")
# writefile.write("what are you doing fifth time?\r\nsecond line")

# writefile.close()
testfile.close()
