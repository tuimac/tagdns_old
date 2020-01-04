#!/usr/bin/env python3

import socket
from endpoint import OutboundEndpoint
from queue import Queue
import time
from threading import Thread
import traceback

LOOP = 10000

class Receiver(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        while True:
            data = sock.recv(4096)
            print(data)
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
    try:
        ip = "127.0.0.1"
        port = 33333
        queue = createQueue(ip, port)
        receiver = Receiver(ip, port)
        receiver.daemon = True
        receiver.start()
        endpoint = OutboundEndpoint(queue, ip, port)
        endpoint.daemon = True
        endpoint.start()
        endpoint.join()
        receiver.join()
    except:
        traceback.print_exc()
