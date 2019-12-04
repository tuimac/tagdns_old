from threading import Thread
from resolve import Resolve
from resolveNode import WorkerNode

class ManageNode():
    def __init__(self, queue, numOfNodes):
        self.queue = queue
        self.numOfNodes = numOfNodes
        mgrNode = Thread(name='runNode', target=runNode())

    def runNode():
        while 

class WorkerNode(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        record = ""
        while record == "":
            record = self.queue.get()
        resolve = Resolve(record)
        result = resolve.resolv()

