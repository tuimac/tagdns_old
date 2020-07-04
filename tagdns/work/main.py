#!/usr/bin/env python3

import logging
import os
from threading import Thread
from queue import Queue
import time

"""
logger = logging.getLogger("tagdns")
logger.setLevel(level=logging.INFO)
"""
queue = Queue()
delete = False

def test1():
    while delete == False:
        print(queue.get())

if __name__ == "__main__":
    q = Thread(target=test)
    q.daemon = True
    q.start()

    time.sleep(1)
    queue.put("hello")
    time.sleep(1)
    delete = True

    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('test.log')
    fh.setLevel(level=logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    sample = Sample()
    sample.sample()
    """
