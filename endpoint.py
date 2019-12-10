import socket
from threading import Thread

class InboundEndpoint(Thread):
    def __init__(self, queue, ip, port):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip
        self.port = port
        self.delete = False
        self.__buffer = 512

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.delete:
            sock.bind((self.ip, self.port))
            data = sock.recvfrom(self.__buffer)
            self.queue.put(data)
        sock.close()

    def delete_socket(self):
        self.delete = True

class OutboundEndpoint(Thread):
    def __init__(self, queue, ip, port):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip
        self.port = port
        self.delete = False

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.delete:
            message = self.queue.get()
            if message == "": continue
            sock.sendto(message[0], message[1])
        sock.close()

    def delete_socket(self):
        self.delete = True
