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
    
    def dns_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        data = sock.recvfrom(512)
        return data

    def run_dns(self):
        for i in range(3):
            worker_node = threading.Thread(target=dns_socket, args=(1,))
            worker_node.start()
