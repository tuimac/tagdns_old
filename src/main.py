#!/usr/bin/env python3

from queue import Queue
from threading import Thread
from init import Init
from utils.exception import ZoneFormatException, ZoneNotFoundException, \
        ConfigNotFoundException, TagKeyNotFoundException, StopNodesError
import time
import os

def stopWholeServices(initData):
    initData["endpoint"].deleteAllSockets()
    initData["resolver"].stopAllNodes()
    initData["autoRenew"].stopNodes()

if __name__ == '__main__':
    initData = ""
    logger = ""
    try:
        confPath = "/home/tuimac/github/tagdns/tagdns.yml"

        initialize = Init(confPath)
        initData = initialize.init()
        
        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        endpoint = initData["endpoint"]
        records = initData["records"]
        resolver = initData["resolver"]
        autoRenew = initData["autoRenew"]
        logger = initData["logger"]

    except KeyboardInterrupt:
        stopWholeServices(initData)

    except ZoneFormatException as e:
        logger.errorLog(e.message, 3)
        stopWholeServices(initData)

    except ConfigNotFoundException as e:
        stopWholeServices(initData)

    except ZoneNotFoundException as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)

    except StopNodesError as e:
        print(e.message, file=sys.stderr)
        stopWholeServices(initData)
