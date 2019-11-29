import socket
from threading import Thread
from threading import Lock
##watch this article
# https://stackoverflow.com/questions/4373728/can-more-than-one-thread-use-the-same-port
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
import re
from queue import Queue

REGEX = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"

class InboundEndpoints(Thread):
    def __init__(self, queue, ip, port):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip
        self.port = port
        self.stop = stop

    def run(self):
        while stop:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.ip, self.port))
            data = sock.recvfrom(512)
            queue.put(data)

class Dns():
    def __init__(self, ip, port):
        if re.search(REGEX, ip) is None:
            self.ip = socket.gethostbyname(ip)
        else:
            self.ip = ip
        self.port = port

    def 


    def run_dns(self):
        queue = Queue()
        for i in range(3):
            print("hello")
            endpoint = InboundEndpoints(queue, self.ip, self.port)
            endpoint.start()
        print(queue.get())
