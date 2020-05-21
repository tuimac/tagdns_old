import socket
from threading import Thread
import time

class Endpoint(Thread):
    def __init__(self, inboundQueue, outboundQueue, config):
        Thread.__init__(self)
        self.inboundQueue = inboundQueue
        self.outboundQueue = outboundQueue
        self.ip = config["ipaddress"]
        self.port = config["port"]
        self.socket = ""
        self.inboundEndpoint = ""
        self.outboundEndpoint = ""

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.inbound = InboundEndpoint(self.inboundQueue, self.ip, self.port, self.socket)
        self.inbound.daemon = True
        self.inbound.start()
        self.outbound = OutboundEndpoint(self.outboundQueue, self.socket)
        self.outbound.daemon = True
        self.outbound.start()
        self.inbound.join()
        self.outbound.join()

    def deleteAllSockets(self):
        self.inbound.deleteSocket()
        self.outbound.deleteSocket()
        print("All sockets had been deleted!")

class InboundEndpoint(Thread):
    def __init__(self, queue, ip, port, socket):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip
        self.port = port
        self.socket = socket
        self.delete = False
        self.__buffer = 512

    def run(self):
        try:
            self.socket.bind((self.ip, self.port))
            while not self.delete:
                data = self.socket.recvfrom(self.__buffer)
                self.queue.put(data)
        except KeyboardInterrupt:
            print("catch")
        
    def deleteSocket(self):
        self.delete = True
        self.socket.close()

class OutboundEndpoint(Thread):
    def __init__(self, queue, socket):
        Thread.__init__(self)
        self.queue = queue
        self.socket = socket
        self.delete = False

    def run(self):
        while not self.delete:
            message = self.queue.get()
            if message == "": continue
            self.socket.sendto(message[0], message[1])

    def deleteSocket(self):
        self.delete = True
        self.socket.close()
