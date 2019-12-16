import binascii
import struct
import sys
import random
import re

from dnslib.dns import *
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
        if re.search(regex, qname) is None:
            qname = self.records.lookupIp(target)
        else:
            qname = self.records.lookupName(target)
        
