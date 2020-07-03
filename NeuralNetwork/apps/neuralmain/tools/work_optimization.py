# from queue import Queue
import sys
import time
from threading import Thread

import datetime

from .analyze_img import save_user_upload
from multiprocessing import Queue, Process


class MyThread(Thread):
    def __init__(self):  # initializing thread
        Thread.__init__(self)

    def run(self):
        time_start = datetime.datetime.now()  # start datetime
        time.sleep(1)  # time to boot thread
        while True:
            time_current = datetime.datetime.now()  # current time
            time_to_wait = 0.5  # minutes

            time.sleep(0.5)
            if not q.empty():
                args = q.get()
                p = Process(target=save_user_upload(img_name=args[0], user_type=args[1]))
                p.start()
                p.join()
                time_start = datetime.datetime.now()  # update datetime

            elif time_current - time_start > datetime.timedelta(minutes=time_to_wait):  # timedelta in min, used 1min
                print(f">>>Thread wait {time_to_wait}min...")
                time.sleep(time_to_wait*60)
                print(">>>Thread wake!")
                # sys.exit()


def put_to_queue(url, user_plant_type):  # this function add external func to queue for run

    if not q.full():  # if queue not full
        q.put([url, user_plant_type])  # add to queue arguments for function save_user_upload

        if not my_thread.isAlive():  # if thread not running
            print(">>>Start thread")
            try:
                my_thread.setDaemon(True)  # set daemon so that the thread closes with the program
                my_thread.start()  # start thread
            except Exception as exc:
                print(">>>Thread error:", exc)
                return str(exc)
    else:
        return 'Queue if full'


q = Queue()
my_thread = MyThread()
