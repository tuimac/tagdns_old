import sys
import random
import re

from dnslib.dns import DNSRecord, DNSHeader, DNSQuestion, RR
from dnslib.label import DNSBuffer

#Look at this RFC article.
# https://tools.ietf.org/html/rfc2929

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.outboundQueue = outboundQueue

    def resolve(self):
        regex = "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?\.)(\w|\W)*"
        buffer = DNSBuffer(self.request)
        header = DNSHeader.parse(buffer)
        question = DNSQuestion.parse(buffer)
        qname = str(question.get_qname())
        target = qname.split(".")[0]
        dRecord = DNSRecord.parse(self.request)
        ttl = "30"
        response = qname + " " + ttl + " "
        if re.search(regex, qname) is None:
            answer = self.records.lookupIp(target)
            response = response + "A " +  answer
        else:
            answer = self.records.lookupName(target)
            response = response + "PTR " + answer
        response = dRecord.replyZone(response)
        response = response.pack()
        print(self.ip)
        print(self.port)
        self.outboundQueue.put((response, (self.ip, self.port)))
