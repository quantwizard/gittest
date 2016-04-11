from subprocess import Popen, PIPE
from time import sleep
from subpro import ErrorCode


def main():
    cmd = ["python", "subpro.py"]
    try:
        sub = Popen(cmd, stdout=PIPE)
        sub.poll()
        while sub.returncode is None:
            output = sub.stdout.readline().strip()
            if output.startswith("111"):
                print output
            elif output == "":
                print "empty"
            elif output is None:
                print "none"
            elif output == "\n":
                print "new line"
            sub.poll()
    except ErrorCode, e:
        print "got ErrorCode: %s" % e
    print "main is over, returncode is %s" % sub.returncode

if __name__ == '__main__':
    main()
