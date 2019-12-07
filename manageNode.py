#from threading import Thread
from resolveNode import WorkerNode
import sys

class ManageNode:
    def __init__(self, queue):
        self.queue = queue
        self.numOfNodes = 4
        self.workerNodes = []
        self.interval = 0.001

    def startNodes(self):
        for x in range(self.numOfNodes):
            node = WorkerNode(self.queue, self.interval)
            node.daemon = True
            node.start()
            self.workerNodes.append(node)

    def stopAllNodes(self):
        for node in self.workerNodes:
            node.stop()
        if len(self.workerNodes) != 0:
            print("Fail to stop", file=sys.stderr)
