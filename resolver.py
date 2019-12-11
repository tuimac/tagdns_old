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
        
        self.resolveName = ""

        self.opcode = Bitwiser.trimBit(request[2], 1, 4)

    def __getQname(self):
        #For skip delimiter of dns host name's flame, trim from 13.
        question = self.request[13:]
        index = 13
        for byte in question:
            if byte < 32: break
            self.resolveName += chr(byte)
            index += 1


    def __getResourceRecord(self):
        pass

    def resolve(self):
        if self.opcode == 0:
            message = Response.stdQuery(self.response, self.records.lookupIp(self.qname), self.ip)
            self.outboundQueue.put(message)
        elif self.opcode == 1:
            print("Inverse Query")
        else:
            print("Othre Query")

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
        
class Response:
    def stdQuery(response, question, dest_ip):
        response = list(response)
        address = (dest_ip, random.randrange(32768, 65535))
        response[2] = Bitwiser.replaceBit(response[2], 0)
        return message

    def createByteResponse():
        pass

