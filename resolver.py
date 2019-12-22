import sys
import random
import re

from dnslib.dns import DNSRecord, DNSHeader, DNSQuestion, RR
from dnslib.label import DNSBuffer

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.outboundQueue = outboundQueue
        self.resultFlag = True

    def __forwardLookup(self, qname):
        result = self.records.lookupIp(qname)
        if result == "": self.resultFlag = False
        result = " A " +  result
        return result
    
    def __reverseLookup(self, qname):
        result = self.records.lookupName(qname)
        if result == "": self.resultFlag = False
        result = " PTR " + result
        return result

    def __createMessage(self, message, response):
        ttl = "30"
        message += " " + ttl
        message += response
        record = DNSRecord.parse(self.request)
        if self.resultFlag is False:
            message = record.replyNameError(message)
        else:
            message = record.replyZone(message)
        return message.pack()

    def resolve(self):
        regex = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?\.)(\w|\W)*"
        response = ""

        buffer = DNSBuffer(self.request)
        header = DNSHeader.parse(buffer)
        question = DNSQuestion.parse(buffer)
        qname = str(question.get_qname())
        if re.search(regex, qname) is None:
            response = self.__forwardLookup(qname)
        else:
            response = self.__reverseLookup(qname)
        message = self.__createMessage(qname, response)
        self.outboundQueue.put((message, (self.ip, self.port)))
