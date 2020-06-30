# from queue import Queue
import sys
import time
from threading import Thread

import datetime

from .analyze_img import save_user_upload
from multiprocessing import Queue


class MyThread(Thread):
    def __init__(self):  # initializing thread
        Thread.__init__(self)
        # self.func = func
        # self.user_plant_type = user_plant_type

    def run(self):
        time_start = datetime.datetime.now()  # start datetime
        while True:
            print("----Cycle RUN----")
            time.sleep(5)  # time to wait
            time_current = datetime.datetime.now()  # current time

            if not q.empty():
                args = q.get()
                save_user_upload(img_name=args[0], user_type=args[1])
                time_start = datetime.datetime.now()  # start datetime

            elif time_current - time_start > datetime.timedelta(minutes=1):  # timedelta in min, used 1min
                print("-----Thread closed-----")
                sys.exit()
                # break
        # save_user_upload(self.url, user_type=self.user_plant_type)


def put_to_queue(url, user_plant_type):  # this function add external func to queue for run
    if not q.full():  # if queue not full
        q.put([url, user_plant_type])  # add to queue arguments for function save_user_upload

        if not my_thread.isAlive():  # if thread not running
            print("Thread dead(")
            try:
                my_thread.start()  # start thread
            except Exception as exc:
                print(exc)
        return_msg = 'Put ok'
    else:
        return_msg = 'Queue if full'
    return return_msg


q = Queue()
my_thread = MyThread()
