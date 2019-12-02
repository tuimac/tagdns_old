from threading import Thread

class GetRequest(Thread):
    def __init__(self, queue):
        self.queue = queue
        
    def workerNode(self, self.queue):
        while self.queue.qsize() > 0:



    def createThread(self):
        
