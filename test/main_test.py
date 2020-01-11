#!/usr/bin/env python3

import subprocess
import threading
import time
import traceback
import logging
import os
import sys
import yaml

from test_ddos import Ddos

FORMAT = "%(levelname)s : %(asctime)s : %(message)s"

class Config:
    def __init__(self):
        configPath = os.path.expanduser("test.yml")
        confFile = open(configPath, "r")
        self.config = yaml.load(confFile)
        confFile.close()

def execMain(path):
    def execute(path): subprocess.call(["python3", path])
    mainThread = threading.Thread(target=execute, name="execute")
    mainThread.start()
    logging.info("Start Main Program")
    time.sleep(3)

if __name__ == '__main__':
    try:
        logging.basicConfig(format=FORMAT)
        config = Config()

        #Start Main Program
        programPath = os.path.expanduser("../src/main.py")
        execMain(prograPath)
        
        #Start Tests
        ## DNS request ddos attack duration test
        ddos = Ddos(config["ddos"])
        ddos.attack()

    except FileNotFoundException:
        logging.error("Can't find files...")
        sys.exit(1)

    except:
        traceback.print_exc()
