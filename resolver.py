import binascii
import struct
import sys
import random

from lab.packet import Packet

#Look at this RFC article.
# https://tools.ietf.org/html/rfc2929

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.records = records
        self.outboundQueue = outboundQueue
        Packet.dumpAll(self.request)

    def resolve(self):
        header = list(self.request[:12])
        #Value of qr in header section turn 0 to 1
        header[2] = Bitwiser.replaceBit(header[2], 0)
        qname = ""
        index = 13
        for index in range(index, len(self.request)):
            if self.request[index] < 32: break
            qname += chr(self.request[index])
        for index in range(index, len(self.request)):
            if self.request[index] == 0: break
        qname = self.records.lookupIp(qname)
        print(qname)
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
        print(test)
        response.append(test)
        response.append(0)
        for byte in list(self.request[index:]):
            response.append(byte)
        print(response)
        message = (bytes(response), (self.ip, self.port))
        print(message)
        self.outboundQueue.put(message)

class Bitwiser:
    def trimBits(bits, start, end):
        answer = bits[start]
        for i in range(start + 1, end + 1): 
            answer = (answer << 8) | bits[i]
        return answer

    def trimBit(bits, start, end, length=8):
        if(start > end):
            print("Argument error.", file=sys.stderr)
            return
        return (bits - ((bits >> (length - start)) << (length - start))) >> (length - end - 1)

    def replaceBit(bits, position, length=8):
        return bits ^ (1 << position)
