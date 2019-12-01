#!/usr/bin/env python3

from threading import Thread
import re
from queue import Queue
from inboundEndpoints import InboundEndpoints
import time

REGEX = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"

if __name__ == '__main__':
    
    ip = '127.0.0.1'
    port = 53
    stop = False

    if re.search(REGEX, ip) is None:
        ip = socket.gethostbyname(ip)

    queue = Queue()
    endpoint = InboundEndpoints(queue, ip, port, stop)
    endpoint.daemon = True
    endpoint.start()
    for i in range(3):
        time.sleep(1)
        print(queue.get())
