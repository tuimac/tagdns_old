from queue import Queue
from endpoint import Endpoint
from records import Records
from manageNodes import ManageNodes
from exception import ZoneFormatException
from config import Config
import re
import queue
import socket

class Initialize():
    def __init__(self, path):
        conf = Config(path)
        config = conf.read()
        self.ip = self.__resolveIP(config["default"]["ip_address"])
        self.port = config["default"]["port"]
        self.path = config["default"]["records_path"]
        self.interval = config["default"]["update_interval"]
        self.numOfNodes = int(config["default"]["worker_threads"])
        self.zone = config["default"]["zones"]
        for zone in self.zone:
            if re.match("\D*\.$", zone) is None: raise ZoneFormatException
        self.inboundQueue = Queue()
        self.outboundQueue = Queue()

    def __resolveIP(self, ip):
        regex= "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        if re.search(regex, ip) is None: ip = socket.gethostbyname(ip)
        return ip

    def __createEndpoint(self):
        endpoint = Endpoint(self.inboundQueue, self.outboundQueue, self.ip, self.port)
        endpoint.daemon = True
        endpoint.start()
        return endpoint

    def __deployRecords(self):
        return Records(self.path, self.zone)

    def __createResolver(self, records):
        mgr = ManageNodes(self.inboundQueue, self.outboundQueue, records, self.numOfNodes)
        return mgr

    def initialize(self):
        initialData = dict()
        initialData["inboundQueue"] = self.inboundQueue
        initialData["outboundQueue"] = self.outboundQueue
        initialData["endpoint"] = self.__createEndpoint()
        initialData["records"] = self.__deployRecords()
        initialData["resolver"] = self.__createResolver(initialData["records"])
        return initialData
