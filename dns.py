import socket
from threading import Thread
##watch this article
# https://stackoverflow.com/questions/4373728/can-more-than-one-thread-use-the-same-port
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
import re
import queue

REGEX = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"

class WorkerNode(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def 

class Dns():
    def __init__(self, ip, port):
        if re.search(REGEX, ip) is None:
            self.ip = socket.gethostbyname(ip)
        else:
            self.ip = ip
        self.port = port
    
    def dns_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        data = sock.recvfrom(512)
        return data

    def run_dns(self):

        for i in range(3):
            print(self)
            worker_node = Thread(name='dns_socket', target=self.dns_socket)
            worker_node.start()
