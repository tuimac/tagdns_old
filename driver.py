#!/usr/bin/env python3

import socket
from endpoint import OutboundEndpoint
from queue import Queue
import time
from threading import Thread

LOOP = 10000

class Receiver(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port

    def run(self):
        for i in range(LOOP):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print(sock)
            sock.bind((self.ip, self.port))
            data = sock.recv(1024)
            print(data)
        print("receiver is ended.")
        sock.close()

def createQueue(ip, port):
    def createMsg(msg, ip, port):
        dest = (ip, port)
        message = (str(msg).encode(), dest)
        return message
    queue = Queue()
    for i in range(LOOP):
        msg = createMsg(i, ip, port)
        queue.put(msg)
    return queue

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 3333
    queue = createQueue(ip, port)
    receiver = Receiver(ip, port)
    receiver.daemon = True
    receiver.start()
    time.sleep(0.5)
    endpoint = OutboundEndpoint(queue, ip, port)
    endpoint.daemon = True
    endpoint.start()
