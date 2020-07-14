from .node import WorkerNode, AutoRenewNode
from .utils.exception import StopNodesError

from threading import Thread

import sys

class ManageResolvNodes(Thread):
    def __init__(self, inboundQueue, outboundQueue, records, logger, config):
        Thread.__init__(self)
        self.inboundQueue = inboundQueue
        self.outboundQueue = outboundQueue
        self.records = records
        self.logger = logger
        self.config = config
        self.numOfNodes = config["worker_threads"]
        self.acl = config["acl"]
        self.workerNodes = []
        self.interval = 0.01

    def run(self):
        for x in range(self.numOfNodes):
            node = WorkerNode(self.inboundQueue, self.outboundQueue, self.interval, \
                            self.records, self.logger, self.config)
            node.daemon = True
            node.start()
            self.workerNodes.append(node)
        [node.join() for node in self.workerNodes]

    def stopAllNodes(self):
        for node in self.workerNodes:
            if node.stop() is False: raise StopNodesError
        print("resolve stop")

class ManageAutoRenewNodes(Thread):
    def __init__(self, records, config):
        Thread.__init__(self)
        self.records = records
        self.config = config
        self.node = ""

    def run(self):
        self.node = AutoRenewNode(self.records, self.config)
        self.node.daemon = True
        self.node.start()
        self.node.join()

    def stopNodes(self):
        if self.node.stop() is False: raise StopNodesError
        print("auto stop")
