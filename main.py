#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from endpoint import InboundEndpoint
import re
import time

REGEX = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"

def createInboundEndpoint(queue, ip, port):
    endpoint = InboundEndpoints(queue, ip, port)
    endpoint.daemon = True
    endpoint.start()

if __name__ == '__main__':
    
    ip = '127.0.0.1'
    port = 53
    stop = False
    recordfile_path = "/home/tuimac/github/dynamic_dns/database.json"

    if re.search(REGEX, ip) is None: ip = socket.gethostbyname(ip)

    request_queue = Queue()
    createInboundEndpoint(request_queue, ip, port)

    

    for i in range(3):
        print(request_queue.get())
