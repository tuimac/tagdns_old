import socket
import logging
import traceback
from queue import Queue
from threading import Thread

logger = logging.getLogger("tagdns")

class Endpoint(Thread):
    def __init__(self, ip=socket.gethostbyname(socket.gethostname()), port=53):
        self,ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    def run(self):
        try:
            self.inbound = Inbound(self.ip, self.port, self.socket)
            self.inbound.daemon = True
            self.inbound.start()
            self.outbound = Outbound(self.socket)
            self.outbound.daemon = True
            self.outbound.start()
        except:
            logger.error(traceback.format_exc())
            return self.response
    
    def getInboundQueue(self):
        return self.inbound.queue

    def getOutboundQueue(self):
        return self.outbound.queue

class Inbound(Thread):
    def __init__(self, ip, port, socket):
        Thread.__init__(self)
        self.queue = Queue()
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        self.__delete = False

    def run(self):
        try:
            self.__socket.__bind((self.__ip, self.__port))
            while not self.__delete:
				data = self.__socket.recvfrom(0xffff)
				self.__queue.put(data)
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
            self.__socket.close()
        except Exception as e:
            raise e

class Outbound(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.queue = Queue()
        self.__socket = socket
        self.__delete = False

    def run(self):
        try:
            while not self.__delete:
                packet = self.queue.get()
                self.__socket.sendto(packet)
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
            self.__socket.close()
        except Exception as e:
            raise e
