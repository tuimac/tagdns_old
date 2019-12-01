import socket
from threading import Thread

class InboundEndpoint(Thread):
    def __init__(self, queue, ip, port):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip
        self.port = port
        self.delete = False

    def run(self):
        while not self.delete:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.ip, self.port))
            data = sock.recvfrom(512)
            self.queue.put(data)
        sock.close()

    def delete_socket(self):
        self.delete = True

class OutboundEndpoint(Thread):
    def __init__(self):
        Thread.__init__(self):
