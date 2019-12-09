import binascii
import struct
import sys

#Look at this RFC article.
# https://tools.ietf.org/html/rfc2929

class Resolver:
    def __init__(self, request, records):
        self.records = records
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = request[0]
        print(len(self.request))
        self.header = {
            "id": 0,
            "qr": 0,
            "opcode": 0,
            "aa": 0,
            "tc": 0,
            "rd": 0,
            "ra": 0,
            "z": 0,
            "rcode": 0
        }
        self.question = {
            "queryCount": 0,
            "answerCount": 0,
            "authRecordCount": 0,

        }
        self.__decodeHeader()
        self.__decodeQuestion()
        #self.__printBit()

    #This method is only for test.
    def __printBit(self):
        binary = bin(int(binascii.hexlify(self.request[0].strip()), 16)).zfill(8)[2:]
        i = 0
        length = len(binary)
        while i < length:
            before = i
            i = i + 16
            print(binary[before:i])

    def __decodeHeader(self):
        header = self.request[:12]

        def bitwise(header, start, end):
            answer = header[start]
            for i in range(start + 1, end + 1):
                answer = (answer << 8) | header[i]
            return answer

        def pickbit(subbyte, start, end, length=8):
            if(start > end): return subbyte
            seed = (subbyte >> (length - start)) << (length - start)
            return (subbyte - seed) >> (length - end - 1)

        self.header["id"] = bitwise(header, 0, 1)
        self.header["qr"] = pickbit(header[2], 0, 0)
        self.header["opcode"] = pickbit(header[2], 1, 4)
        self.header["aa"] = pickbit(header[2], 5, 5)
        self.header["tc"] = pickbit(header[2], 6, 6)
        self.header["rd"] = pickbit(header[2], 7, 7)
        self.header["ra"] = pickbit(header[3], 0, 0)
        self.header["z"] = pickbit(header[3], 1, 3)
        self.header["rcode"] = pickbit(header[3], 4, 7)

    def __decodeQuestion(self):
        question = self.request[12:]

    
        
    def resolve(self):
        pass
