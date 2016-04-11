import os
import signal

def write_pid():
    pid = os.getpid()
    print pid
    with open('test.pid', 'w') as f:
        f.write(str(pid))

def kill():
    with open('test.pid', 'r') as f:
        for pid in f:
            os.kill(int(pid), signal.SIGTERM)

def main():
    write_pid()
    kill()

if __name__ == '__main__':
    main()