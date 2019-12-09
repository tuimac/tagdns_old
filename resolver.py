import binascii
import struct
import sys
#from dnslib.dns import DNSRecord

FILTER = bytearray([ (i < 32 or i > 127) and 46 or i for i in range(256) ])

class Resolver:
    def __init__(self, request, records):
        self.records = records
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        self.header = request[0][:12]
        self.question = request[0][12:]
        self.binary = bin(int(binascii.hexlify(request[0].strip()), 16)).zfill(8)[2:]

    def resolve(self):
        i = 0
        length = len(self.binary)
        while i < length:
            before = i
            i = i + 16
            print(self.binary[before:i])

        self.decodeHeader(self.header)
        self.decodeQuestion(self.question)

    def decodeHeader(self, header):
        def bitwise(header, start, end):
            answer = header[start]
            for i in range(start + 1, end + 1):
                answer = (answer << 8) | header[i]
            return answer

        def pickbit(subbyte, start, end, length=8):
            if(start > end): return subbyte
            seed = (subbyte >> (length - start)) << (length - start)
            return (subbyte - seed) >> (length - end - 1)

        print("id", bitwise(header, 0, 1))
        print("qr", pickbit(header[2], 0, 0))
        print("opcode", pickbit(header[2], 1, 4))
        print("aa", pickbit(header[2], 5, 5))
        print("tc", pickbit(header[2], 6, 6))
        print("rd", pickbit(header[2], 7, 7))
        print("ra", pickbit(header[3], 0, 0))
        print("z", pickbit(header[3], 1, 3))
        print("rcode", pickbit(header[3], 4, 7))

    def decodeQuestion(self, request):

        pass
