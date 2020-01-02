#!/usr/bin/env python3

from queue import Queue
from threading import Thread
from init import Init
from utils.exception import ZoneFormatException, ZoneNotFoundException, \
        ConfigNotFoundException, TagKeyNotFoundException, StopNodesError
import time
import os
import syslog
import traceback

def stopWholeServices(initData):
    initData["endpoint"].deleteAllSockets()
    initData["resolver"].stopAllNodes()
    initData["autoRenew"].stopNodes()

if __name__ == '__main__':
    initData = ""
    try:
        confPath = "/home/tuimac/github/tagdns/tagdns.yml"

        initialize = Init(confPath)
        initData = initialize.init()
         
        logger = initData["logger"]       
        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        endpoint = initData["endpoint"]
        records = initData["records"]
        resolver = initData["resolver"]
        autoRenew = initData["autoRenew"]
        logger = initData["logger"]

    except ZoneFormatException as e:
        syslog.syslog(syslog.LOG_ERR, e.message)

    except ConfigNotFoundException as e:
        syslog.syslog(syslog.LOG_ERR, e.message)
        stopWholeServices(initData)

    except ZoneNotFoundException as e:
        logger.errorLog(e.message, 2)
        stopWholeServices(initData)

    except StopNodesError as e:
        logger.errorLog(e.message, 1)
        stopWholeServices(initData)

    except Exception as e:
        syslog.syslog(syslog.LOG_ERR, traceback.format_exc().splitlines()[-1])
        stopWholeServices(initData)
