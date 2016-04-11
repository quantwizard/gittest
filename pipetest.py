from multiprocessing import Process, Pipe
from time import sleep

def f(conn):
    times = 5
    while times > 0:
        conn.send([times, None, 'hello'])
        sleep(1)
        times -= 1
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    data = parent_conn.recv()
    print data
    while data:
        # recv() will block there even pipe is closed
        # so we have to know how many times the child_conn send data, we do exactly
        # same times recv()
        data = parent_conn.recv()   # prints "[42, None, 'hello']"
        print data
        print type(data)
    p.join()