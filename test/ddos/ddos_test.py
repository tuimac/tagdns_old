import socket
import time
from threading import Thread
import traceback

class Ddos:
    class ResultList(list):
        def __init__(self): pass

    def __init__(self, targetip, targetport, ip):
        self.nodes = []
        self.portRange = 65535
        self.args = dict()
        self.args["targetip"] = targetip
        self.args["targetport"] = int(targetport)
        self.args["ip"] = ip
        self.args["numOfPacket"] = 3

    def attack(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        resultList = ResultList()
        resultList = [None] * self.portRange
        analyzer = Analyzer()
        self.args["message"] = analyzer.sendMsg()
        for port in range(self.portRange):
            try:
                self.args["port"] = port
                sock.bind((self.args["ip"], port))
                self.args["socket"] = sock
                attacker = Attcker(self.args, resultList)
                attacker.daemon = True
                attacker.start()
                self.nodes.append(attacker)
            except:
                traceback.print_exc()
        [node.join() for node in self.nodes]
        analyzer = Analyzer(resultList)

class Attacker(Thread):
    def __init__(self, args, resultList):
        Thread.__init__(self)
        self.args = args
        self.resultList = resultList
        self.result = dict()

    def run(self):
        socket = self.args["socket"]
        self.sendPacket(socket)
        self.resultList.insert(self.result, self.args["port"])
   
    def sendPacket(self, socket):
        execTime = [0] * self.args["numOfPacket"]
        results = [None] * self.args["numOfPacket"]
        for i in range(self.args["numOfPacket"])):
            start = time.time()
            socket.sendto(message, (self.args["targetip"], self.args.["targetport"]))
            result = self.socket.recvfrom(4096)
            end = time.time()
            execTime = end - start
            results.append(result)
        self.result["execTime"] = execTime
        self.result["packet"] = results

class Analyzer:
    def __init__(self, results):
        self.results = results

    def checkPacket(self):
        for result in self.results:
            print(result["packet"])
        
    def calcMeanExecTime(self):
        pass
