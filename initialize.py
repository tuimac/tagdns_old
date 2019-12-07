from configparser import ConfigParser
from queue import Queue

from endpoint import InboundEndpoint
from records import Records
from manageNode import ManageNode

import re
import socket

class Initialize():
    def __init__(self, path):
        config = ConfigParser()
        config.read(path)
        self.ip = self.__resolveIP(config["Default"]["ipaddress"])
        self.port = int(config["Default"]["port"])
        self.path = config["Default"]["recordsPath"]
        self.queue = Queue()

    def __resolveIP(self, ip):
        regex= "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        if re.search(regex, ip) is None: ip = socket.gethostbyname(ip)

        return ip

    def __createInboundEndpoint(self):
        endpoint = InboundEndpoint(self.queue, self.ip, self.port)
        endpoint.daemon = True
        endpoint.start()

        return endpoint

    def __createOutboundEndpoint(self):
        pass

    def __deployRecords(self):
        return Records(self.path)

    def __createResolver(self):
        mgr = ManageNode(self.queue)
        mgr.startNodes()
        import time
        time.sleep(5)
        mgr.stopAllNodes()

    def initialize(self):
        initialData = dict()
        initialData["requestQueue"] = self.queue
        initialData["inboundEndpoint"] = self.__createInboundEndpoint()
        initialData["outboundEndpoint"] = self.__createOutboundEndpoint()
        initialData["records"] = self.__deployRecords()
        initialData["resolver"] = self.__createResolver()

        return initialData
