from .dnslib.dns import DNSRecord, DNSHeader, DNSQuestion, RR
from .dnslib.label import DNSBuffer
from .getRecord import GetRecord
from .utils.acl import Acl

import sys

class Resolver:
    def __init__(self, request, outboundQueue, records, logger, config):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.logger = logger
        self.acl = config["acl"]
        self.outboundQueue = outboundQueue
        self.resultFlag = True

    def __createMessage(self, message, response, rcode):
        ttl = "30"
        message += " " + ttl
        message += response
        record = DNSRecord.parse(self.request)
        if rcode == 16:
            message = record.replyZone(message)
        else:
            message = record.replyWithRcode(message, rcode=rcode)
        return message.pack()

    def resolve(self):
        buffer = DNSBuffer(self.request)
        header = DNSHeader.parse(buffer)
        question = DNSQuestion.parse(buffer)
        qname = str(question.get_qname())
        qtype = question.get_qtype()

        response = ""
        rcode = 0

        if len(self.acl) > 0 and Acl.filter(self.ip, self.acl) == 5:
            logMsg = " SourceIP: " + self.ip + " SourcePort: " + \
                       str(self.port) + " Access was denied."
            self.logger.accessLog(logMsg, 1)
            response = ""
            rcode = 5
        else:
            logMsg = " SourceIP: " + self.ip + " SourcePort: " + str(self.port)
            self.logger.accessLog(logMsg, 4)
            response, rcode = self.records.getRecord(qtype, qname)

        message = self.__createMessage(qname, response, rcode)
        self.outboundQueue.put((message, (self.ip, self.port)))
        return
