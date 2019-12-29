from threading import Thread
import time
from resolver import Resolver
from autoRenew import AutoRenew

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
        while True:
            if self.stopSignal is True: return self.stopSignal
            time.sleep(self.interval)

class AutoRenewNode(Thread):    
    def __init__(self, records, interval, zone):
        Thread.__init__(self)
        self.records = records
        self.interval = interval
        self.zone = zone
        self.flag = True
        self.stopSignal = False

    def run(self):
        autoRenew = AutoRenew(self.records, self.zone)
        while self.flag:
            autoRenew.autoRenewRecords()
            time.sleep(self.interval)
        self.stopSignal = True
        
    def stop(self):
        self.flag = False
        while True:
            if self.stopSignal is True: return self.stopSignal
            time.sleep(1)
