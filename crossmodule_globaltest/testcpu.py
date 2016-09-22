import getcpu
from time import sleep


def main():
    while 1:
        print getcpu.get_cpu()
        sleep(5)


if __name__ == '__main__':
    main()
