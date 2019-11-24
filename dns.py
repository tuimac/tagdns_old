import socketserver
import threading

class UDPHandler(socketserver.BaseRequestHandler):
    def handler(self):
        return self.request[0].strip()

class Dns():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def run_dns(self):
        with socketserver.UDPServer((self.host, self.port), UDPHandler) as server:
            server.serve_forever()
