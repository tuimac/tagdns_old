#!/usr/bin/env python3

from queue import Queue
from threading import Thread
from functools import partial
from initialize import Initialize
from exception import ZoneFormatException, ZoneNotFoundException, \
        ConfigNotFoundException, TagKeyNotFoundException, StopNodesError
import time
import os
import sys
import traceback

def stopWholeServices(initData):
    initData["endpoint"].deleteAllSockets()
    initData["resolver"].stopAllNodes()
    initData["autoRenew"].stopNodes()

if __name__ == '__main__':
    initData = ""
    try:
        confPath = "/etc/tagdns.yml"

        init = Initialize(confPath)
        initData = init.initialize()
        
        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        endpoint = initData["endpoint"]
        records = initData["records"]
        resolver = initData["resolver"]
        autoRenew = initData["autoRenew"]

    except KeyboardInterrupt:
        stopWholeServices(initData)

    except ZoneFormatException as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)

    except ConfigNotFoundException as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)

    except ZoneNotFoundException as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)

    except StopNodesError as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)
