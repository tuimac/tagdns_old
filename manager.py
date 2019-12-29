#from threading import Thread
from node import WorkerNode, AutoRenewNode
from exception import StopNodesError
from threading import Thread
import sys

class ManageResolvNodes(Thread):
    def __init__(self, inboundQueue, outboundQueue, records, numOfNodes):
        Thread.__init__(self)
        self.inboundQueue = inboundQueue
        self.outboundQueue = outboundQueue
        self.records = records
        self.numOfNodes = numOfNodes
        self.workerNodes = []
        self.interval = 0.01

    def run(self):
        for x in range(self.numOfNodes):
            node = WorkerNode(self.inboundQueue, self.outboundQueue, self.interval, self.records)
            node.daemon = True
            node.start()
            self.workerNodes.append(node)
        [node.join() for node in self.workerNodes]

    def stopAllNodes(self):
        for node in self.workerNodes:
            if node.stop() is False: raise StopNodesError

class ManageAutoRenewNodes(Thread):
    def __init__(self, records, interval, zone):
        Thread.__init__(self)
        self.records = records
        self.interval = interval
        self.zone = zone
        self.node = ""

    def run(self):
        self.node = AutoRenewNode(self.records, self.interval, self.zone)
        self.node.daemon = True
        self.node.start()
        self.node.join()

    def stopNodes(self):
        if self.node.stop() is False: raise StopNodesError
