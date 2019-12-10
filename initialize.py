from configparser import ConfigParser
from queue import Queue

from endpoint import InboundEndpoint
from endpoint import OutboundEndpoint
from records import Records
from manageNodes import ManageNodes

import re
import socket
import queue

class Initialize():
    def __init__(self, path):
        config = ConfigParser()
        config.read(path)
        self.ip = self.__resolveIP(config["Default"]["ipaddress"])
        self.port = int(config["Default"]["port"])
        self.path = config["Default"]["recordsPath"]
        self.interval = config["Default"]["update_interval"]
        self.inboundQueue = Queue()
        self.outboundQueue = Queue()

    def __resolveIP(self, ip):
        regex= "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        if re.search(regex, ip) is None: ip = socket.gethostbyname(ip)

        return ip

    def __createInboundEndpoint(self):
        endpoint = InboundEndpoint(self.inboundQueue, self.ip, self.port)
        endpoint.daemon = True
        endpoint.start()

        return endpoint

    def __createOutboundEndpoint(self):
        endpoint = OutboundEndpoint(self.outboundQueue, self.ip, self.port)
        endpoint.daemon = True
        endpoint.start()

        return endpoint

    def __deployRecords(self):
        return Records(self.path)

    def __createResolver(self, records):
        mgr = ManageNodes(self.inboundQueue, self.outboundQueue, records)
        mgr.startNodes()
        # This code is for test below
        import time
        time.sleep(7)
        mgr.stopAllNodes()

    def initialize(self):
        initialData = dict()
        initialData["inboundQueue"] = self.inboundQueue
        initialData["outboundQueue"] = self.outboundQueue
        initialData["inboundEndpoint"] = self.__createInboundEndpoint()
        initialData["outboundEndpoint"] = self.__createOutboundEndpoint()
        initialData["records"] = self.__deployRecords()
        initialData["resolver"] = self.__createResolver(initialData["records"])

        return initialData
