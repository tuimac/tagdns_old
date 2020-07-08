import socket
import logging
import traceback
import random
import string
import time
from queue import Queue
from threading import Thread

logger = logging.getLogger("tagdns")

class Endpoint(Thread):
    def __init__(self, ip=socket.gethostbyname(socket.gethostname()), port=53):
        Thread.__init__(self)
        self.__ip = ip
        self.__port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.inbound = None
        self.outbound = None

    def run(self):
        try:
            self.inbound = Inbound(self.__ip, self.__port, self.socket)
            self.inbound.daemon = True
            self.inbound.start()
            self.outbound = Outbound(self.socket)
            self.outbound.daemon = True
            self.outbound.start()
        except:
            raise
            #logger.error(traceback.format_exc())
    
    def getInboundQueue(self):
        return self.inbound.queue

    def getOutboundQueue(self):
        return self.outbound.queue

    def closeAllEndpoint(self):
        try:
            self.inbound.closeEndpoint()
            self.outbound.closeEndpoint()
        except:
            raise
            #logger.error(traceback.format_exc())

class Inbound(Thread):
    def __init__(self, ip, port, socket):
        Thread.__init__(self)
        self.queue = Queue()
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        self.__secret = ""

    def run(self):
        try:
            self.__socket.__bind((self.__ip, self.__port))
            while True:
                data = self.__socket.recvfrom(0xffff)
                if data[0] == self.__secret: break
                self.__queue.put(data)
        except:
            raise

    def closeEndpoint(self):
        try:
            self.__delete = True
            all = string.ascii_letters + string.digits + string.punctuation
            self.__secret = ''.join(random.choice(all) for i in range(10)).encode('utf-8')
            self.__socket.sendto(self.__secret, (self.__ip, self.__port))
            self.__socket.close()
        except:
            raise

class Outbound(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.queue = Queue()
        self.__socket = socket
        self.__secret = 0

    def run(self):
        try:
            while True:
                packet = self.queue.get()
                if packet == self.__secret: break
                self.__socket.sendto(packet)
        except:
            raise

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__secret = random.random()
            self.queue.put(self.__secret)
            self.__queue.put()
            self.__socket.close()
        except:
            raise
