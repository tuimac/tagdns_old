import socket
import threading
##watch this article
# https://stackoverflow.com/questions/4373728/can-more-than-one-thread-use-the-same-port
import re
import queue

REGEX = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"

class Dns():
    def __init__(self, ip, port):
        if re.search(REGEX, ip) is None:
            self.ip = socket.gethostbyname(ip)
        else:
            self.ip = ip
        self.port = port
    
    def run_dns(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        data, addr = sock.recvfrom(512)
        print(addr)
        return data
