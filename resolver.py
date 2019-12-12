import binascii
import struct
import sys
import random

#Look at this RFC article.
# https://tools.ietf.org/html/rfc2929

class Resolver:
    def __init__(self, request, outboundQueue, records):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        print(request)
        self.records = records
        self.outboundQueue = outboundQueue

    def resolve(self):
        header = list(self.request[:12])
        #Value of qr in header section turn 0 to 1
        header[2] = Bitwiser.replaceBit(header[2], 0)
        qname = ""
        index = 13
        for i in range(13, len(self.request)):
            if self.request[i] < 32: break
            qname += chr(self.request[i])
            index += 1
        print(index)
        qname = self.records.lookupIp(qname)

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
