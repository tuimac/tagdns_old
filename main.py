#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from functools import partial
from initialize import Initialize
from exception import ZoneFormatException, ZoneNotFoundException, ConfigNotFoundException, TagKeyNotFoundException, StopNodesError
import time
import os
import sys
import traceback

if __name__ == '__main__':
    initData = ""
    try:
        confPath = "tagdns.yml"

        init = Initialize(confPath)
        initData = init.initialize()
        
        inboundQueue = initData["inboundQueue"]
        outboundQueue = initData["outboundQueue"]
        endpoint = initData["endpoint"]
        records = initData["records"]
        resolver = initData["resolver"]
        autoRenew = initData["autoRenew"]

    except FileNotFoundError:
        print("Maybe tagdns.ini is wrong...")

    except KeyboardInterrupt:
        initData["endpoint"].deleteAllSockets()
        print("hello")
        initData["resolver"].stopAllNodes()
        initData["autoRenew"].stopNodes()

    except ZoneFormatException as e:
        print(e.message, file=sys.stderr)

    except ConfigNotFoundException as e:
        print(e.message, file=sys.stderr)

    except ZoneNotFoundException as e:
        print(e.message, file=sys.stderr)

    except StopNodesError as e:
        print(e.message, file=sys.stderr)

    except:
        traceback.print_exc()
