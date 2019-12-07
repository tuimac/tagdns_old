from threading import Thread
from resolver import Resolver
import time

class WorkerNode(Thread):
    def __init__(self, queue, interval):
        Thread.__init__(self)
        self.queue = queue
        self.interval = interval
        self.flag = True
        self.stopSignal = False

    def run(self):
        while self.flag:
            if self.queue.qsize() == 0:
                time.sleep(self.interval * 10)
                continue
            request = self.queue.get()
            self.queue.task_done()
            resolver = Resolver(request)
            resolver.resolve()
        self.stopSignal = True

    def stop(self):
        self.flag = False
        time.sleep(0.5)
        return self.stopSignal
