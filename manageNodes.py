#from threading import Thread
from node import WorkerNode
import sys

class ManageNodes:
    def __init__(self, queue, records):
        self.records = records
        self.queue = queue
        self.numOfNodes = 4
        self.workerNodes = []
        self.interval = 0.001

    def startNodes(self):
        for x in range(self.numOfNodes):
            node = WorkerNode(self.queue, self.interval, self.records)
            node.daemon = True
            node.start()
            self.workerNodes.append(node)

    def stopAllNodes(self):
        for node in self.workerNodes:
            if node.stop() is False:
                print("Fail to stop", file=sys.stderr)
                return
            print("Stop node has been successed!")