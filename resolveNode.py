from threading import Thread
from resolve import Resolve

class ManageNode():
    def runNode(self, queue):
        


class WorkerNode(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        record = ""
        while record == "":
            record = queue.get()
        result = Resolve.get
