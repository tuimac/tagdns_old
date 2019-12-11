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
        self.response = request[0]
        #print(len(self.request))
        print(self.request)
        self.header = {
            "id": 0, "qr": 0, "opcode": 0,
            "aa": 0, "tc": 0, "rd": 0, "ra": 0,
            "z": 0, "rcode": 0, "qdcount": 0,
            "ancount": 0, "nscount": 0, "arcount": 0
        }
        self.__decodeHeader()
        self.hostname = self.__decodeQuestion()
        self.__printBit()
        self.records = records
        self.outboundQueue = outboundQueue

    #This method is only for test.
    def __printBit(self):
        binary = bin(int(binascii.hexlify(self.request.strip()), 16)).zfill(8)[2:]
        i = 0
        header_index = 0
        length = len(binary)
        print("[header]")
        while i < length:
            if header_index == 6: print("\n[Question]")
            before = i
            i = i + 16
            print(binary[before:i])
            header_index += 1

    def __decodeHeader(self):
        header = self.request[:12]
        self.header["id"] = Bitwiser.trimBits(header, 0, 1)
        self.header["qr"] = Bitwiser.trimBit(header[2], 0, 0)
        self.header["opcode"] = Bitwiser.trimBit(header[2], 1, 4)
        self.header["aa"] = Bitwiser.trimBit(header[2], 5, 5)
        self.header["tc"] = Bitwiser.trimBit(header[2], 6, 6)
        self.header["rd"] = Bitwiser.trimBit(header[2], 7, 7)
        self.header["ra"] = Bitwiser.trimBit(header[3], 0, 0)
        self.header["z"] = Bitwiser.trimBit(header[3], 1, 3)
        self.header["qdcount"] = Bitwiser.trimBits(header, 4, 5)
        self.header["ancount"] = Bitwiser.trimBits(header, 6, 7)
        self.header["nscount"] = Bitwiser.trimBits(header, 8, 9)
        self.header["arcount"] = Bitwiser.trimBits(header, 10, 11)
        print(self.header)

    def __decodeQuestion(self):
        #For skip delimiter of dns host name's flame, trim from 13.
        question = self.request[13:]
        name = ""
        for byte in question:
            if byte < 32: break
            name += chr(byte)
        return name
        
    def resolve(self):
        if self.header["opcode"] == 0:
            message = Response.stdQuery(self.records.lookupIp(self.hostname), self.ip)
            self.outboundQueue.put(message)
        elif self.header["opcode"] == 1:
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

    def replaceBit(bits, start, end, length=8):
        pass
        
class Response:
    def stdQuery(response, dest_ip):
        address = (dest_ip, random.randrange(32768, 65535))
