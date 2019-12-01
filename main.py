#!/usr/bin/env python3

from threading import Thread
from queue import Queue

from initialize import Initialize

import time
import os
import sys

if __name__ == '__main__':

    initPath = "tagdns.ini"
    if os.path.exists(initPath) is False:
        print("There is no init file.", file=sys.stderr)
        exit(1)

    initialData = Initialize(initPath)

    ip = initialData.ip
    port = initialData.port
    path = initialData.path
    delete = False

    initData = initialData.initialize()

    inboundEndpoint = initData["InboundEndpoint"]
    requestQueue = initData["requestQueue"]

    for i in range(3):
        print(requestQueue.get())
