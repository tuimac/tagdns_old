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

if __name__ == '__main__':
    initData = ""
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
        
        print("Initialization has been done.")
        
        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        endpoint = initData["endpoint"]
        records = initData["records"]
        resolver = initData["resolver"]

        resolver.startNodes()

    except FileNotFoundError:
        print("Maybe tagdns.ini is wrong...")

    except KeyboardInterrupt:
        print("Catch the exception.")
        initData["resolver"].stopAllNodes()
        initData["endpoint"].deleteAllSockets()

    except:
        traceback.print_exc()
