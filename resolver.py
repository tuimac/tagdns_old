import sys

from dnslib.dns import DNSRecord, DNSHeader, DNSQuestion, RR
from dnslib.label import DNSBuffer
from database import GetRecord

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.outboundQueue = outboundQueue
        self.resultFlag = True

    def __createMessage(self, message, response, searchResult):
        ttl = "30"
        message += " " + ttl
        message += response
        record = DNSRecord.parse(self.request)
        if searchResult is False:
            message = record.replyWithRcode(message)
        else:
            message = record.replyZone(message)
        return message.pack()

    def resolve(self):
        response = ""
        buffer = DNSBuffer(self.request)
        header = DNSHeader.parse(buffer)
        question = DNSQuestion.parse(buffer)
        qname = str(question.get_qname())
        qtype = question.get_qtype()
        #if qtype < 1 or qtype > 16: return
        response = self.records.getRecord(qtype, qname)
        message = self.__createMessage(qname, response[0], response[1])
        self.outboundQueue.put((message, (self.ip, self.port)))
        return
