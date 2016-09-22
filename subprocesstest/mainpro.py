from subprocess import Popen, PIPE, STDOUT
from time import sleep
from subpro import ErrorCode


def main():
    cmd = ["python", "subpro.py"]
    try:
        sub = Popen(cmd, stdout=PIPE, stderr=STDOUT)
        sleep(20)
        stdout, stderr = sub.communicate()
        print stdout
        # sub.kill()
        # sub.poll()
        # while sub.returncode is None:
        #     output = sub.stdout.readline().strip()
        #     if output.startswith("111"):
        #         print output
        #     elif output == "":
        #         print "empty"
        #     elif output is None:
        #         print "none"
        #     elif output == "\n":
        #         print "new line"
        #     sub.poll()
    except ErrorCode, e:
        print "got ErrorCode: %s" % e
    print "main is over, returncode is %s" % sub.returncode


def main2():
    try:
        pro = Popen(["python", "subpro.py"], stdout=PIPE, stderr=PIPE)
        stdout, stderr = pro.communicate()
        print stdout
    except:
        pro.kill()
        pro.wait()
        raise
    retcode = pro.poll()
    if retcode:
        print "returncode is : %d" % retcode

if __name__ == '__main__':
    main2()

