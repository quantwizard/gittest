import threading
import psutil

global cpu
cpu = 0


class CpuMonitorThread(threading.Thread):
    def run(self):
        global cpu_usage
        while 1:
            cpu_usage = get_cpu_usage()


def get_cpu_usage():
    """This function is used to get cpu usage percent.
    if the us+sys cpu usage is 90%, it will return 90.0"""
    return psutil.cpu_percent(3)


def get_cpu():
    global cpu
    return cpu

if __name__ == "__main__":
    cpu_monitor = CpuMonitorThread()
    cpu_monitor.setDaemon(True)
    cpu_monitor.start()
