#from threading import Thread
from node import WorkerNode
import sys

class ManageNodes:
    def __init__(self, inboundQueue, outboundQueue, records, numOfNodes):
        self.inboundQueue = inboundQueue
        self.outboundQueue = outboundQueue
        self.records = records
        self.numOfNodes = numOfNodes
        self.workerNodes = []
        self.interval = 0.001

    def startNodes(self):
        for x in range(self.numOfNodes):
            node = WorkerNode(self.inboundQueue, self.outboundQueue, self.interval, self.records)
            node.daemon = True
            node.start()
            self.workerNodes.append(node)
        [node.join() for node in self.workerNodes]

    def stopAllNodes(self):
        for node in self.workerNodes:
            if node.stop() is False:
                print("Fail to stop", file=sys.stderr)
                return
            print("Stop node has been successed!")
