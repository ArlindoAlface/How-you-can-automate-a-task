import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())


schedule.every().monday.at('15:15').do(task)


while True:
    schedule.run_pending()
    time.sleep(1)