import schedule
import time


def job():
    print("I'm working...")


schedule.every().hour.at(':26').do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)
