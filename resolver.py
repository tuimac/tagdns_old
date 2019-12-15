import binascii
import struct
import sys
import random

from lab.packet import Packet
from lab.bitwiser import Bitwiser

#Look at this RFC article.
# https://tools.ietf.org/html/rfc2929

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.outboundQueue = outboundQueue

        ###Analyze section###
        packet = Packet(self.request)
        packet.dumpBits()
        packet.dumpPacket()

    def resolve(self):
        header = list(self.request[:12])
        #Value of qr in header section turn 0 to 1
        header[2] = Bitwiser.flipBit(header[2], 0)
        qname = ""
        index = 13
        for index in range(index, len(self.request)):
            if self.request[index] < 32: break
            qname += chr(self.request[index])
        for index in range(index, len(self.request)):
            if self.request[index] == 0: break
        qname = self.records.lookupIp(qname)
        if qname == "": return
        response = header
        response.append(1)
        tmp = ""
        for i in range(len(qname)):
            if qname[i] == '.':
                response.append(int(tmp.encode('ascii'), base=10) + 48)
                response.append(1)
                tmp = ""
                continue
            tmp += qname[i]
        test = int(tmp.encode('ascii'), base=10) + 48
        response.append(test)
        response.append(0)
        for byte in list(self.request[index:]):
            response.append(byte)
        print(response)
        message = (bytes(response), (self.ip, self.port))
        self.outboundQueue.put(message)
