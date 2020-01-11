#!/usr/bin/env python3

import subprocess
import threading
import time
import traceback
import logging
import os
import sys

from test_ddos import Ddos

FORMAT = "%(levelname)s : %(asctime)s : %(message)s"

def execMain(path):
    def execute(path): subprocess.call(["python3", path])
    mainThread = threading.Thread(target=execute, name="execute")
    mainThread.start()
    logging.info("Start Main Program")
    time.sleep(3)

if __name__ == '__main__':
    try:
        logging.basicConfig(format=FORMAT)

        #Start Main Program
        programPath = os.path.expanduser("../src/main.py")
        execMain(prograPath)
        
        #Start Tests
        ddos = Ddos("192.168.10.3", 53, "1992.168.10.5")
        ddos.attack()

    except FileNotFoundException:
        logging.error("Can't find main.py...")
        sys.exit(1)

    except:
        traceback.print_exc()
