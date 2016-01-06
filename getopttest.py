import getopt
import sys


def main():
    shortopts = "hs:d:" # there is no : after h, that means no parameter
    longopts = ["help", "say=", "do="]  # there is = means shall have parameter
    optlist, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    print optlist
    print args

if __name__ == '__main__':
    main()