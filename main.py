#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from functools import partial

from initialize import Initialize

import time
import os
import sys
import traceback
import signal

def signal_handler(resolver, signum, frame):
    resolver.stopAllNodes()
    return

if __name__ == '__main__':
    try:
        initPath = "tagdns.ini"
        if os.path.exists(initPath) is False:
            print("There is no init file.", file=sys.stderr)
            exit(1)

        initialData = Initialize(initPath)

        ip = initialData.ip
        port = initialData.port
        path = initialData.path

        initData = initialData.initialize()

        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        inboundEndpoint = initData["inboundEndpoint"]
        outboundEndpoint = initData["outboundEndpoint"]
        records = initData["records"]
        resolver = initData["resolver"]

        signal.signal(signal.SIGINT, partial(signal_handler, resolver))

    except FileNotFoundError:
        print("Maybe tagdns.ini is wrong...")

    except:
        traceback.print_exc()
