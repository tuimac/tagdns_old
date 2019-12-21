from threading import Thread
from resolver import Resolver
import time

class WorkerNode(Thread):
    def __init__(self, inboundQueue, outboundQueue, interval, records):
        Thread.__init__(self)
        self.inboundQueue = inboundQueue
        self.outboundQueue = outboundQueue
        self.records = records
        self.interval = interval
        self.flag = True
        self.stopSignal = False

    def run(self):
        while self.flag:
            if self.inboundQueue.qsize() == 0:
                time.sleep(self.interval * 10)
                continue
            request = self.inboundQueue.get()
            self.inboundQueue.task_done()
            if request == "": continue
            resolver = Resolver(request, self.outboundQueue, self.records)
            resolver.resolve()
        self.stopSignal = True

    def stop(self):
        self.flag = False
        self.inboundQueue.put("")
        time.sleep(0.5)
        return self.stopSignal
