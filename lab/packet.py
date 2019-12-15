import binascii
import json
from lab.bitwiser import Bitwiser

class Packet:
    
    def __init__(self, packet):
        self.packet = packet
        self.dumpFormat = {
            "header": {},
            "question": {},
            "answer": {},
            "authority": {},
            "additional": {}
        }
        self.answerIndex = 0
        self.authorityIndex = 0
        self.additionalIndex = 0

        self.__setHeader()
        self.__setQuestion()
        #self.__setAnswer()
        #self.__setAuthority()
        #self.__setAdditional()

    def dumpBits(self, digits=16):
        binary = bin(int(binascii.hexlify(self.packet.strip()), 16)).zfill(8)[2:]
        i = 0
        header_index = 0
        length = len(binary)
        print("[header]")
        while i < length:
            if header_index == 96: print("\n[Question]")
            before = i
            i = i + int(digits / 2)
            print(binary[before:i], end = " ")
            before = i
            i = i + int(digits / 2)
            print(binary[before:i])
            header_index += digits * (int(digits / 8))

    def dumpPacket(self):
        def jsonDump(data):
            print(json.dumps(data,
                default=True,
                ensure_ascii=False,
                indent=4,
                separators=(',', ': ')
            ))
        jsonDump(self.dumpFormat)

    def __setHeader(self):
        self.dumpFormat["header"]["id"] = Bitwiser.bitsToDecimal(self.packet, 0)
        self.dumpFormat["header"]["qr"] = Bitwiser.bitsToDecimal(self.packet, 1, 0, 0)
        self.dumpFormat["header"]["opcode"] = Bitwiser.bitsToDecimal(self.packet, 1, 1, 4)
        self.dumpFormat["header"]["aa"] = Bitwiser.bitsToDecimal(self.packet, 1, 5, 5)
        self.dumpFormat["header"]["tc"] = Bitwiser.bitsToDecimal(self.packet, 1, 6, 6)
        self.dumpFormat["header"]["rd"] = Bitwiser.bitsToDecimal(self.packet, 1, 7, 7)
        self.dumpFormat["header"]["ra"] = Bitwiser.bitsToDecimal(self.packet, 1, 8, 8)
        self.dumpFormat["header"]["z"] = Bitwiser.bitsToDecimal(self.packet, 1, 9, 11) 
        self.dumpFormat["header"]["rcode"] = Bitwiser.bitsToDecimal(self.packet, 1, 12, 15) 
        self.dumpFormat["header"]["qdcount"] = Bitwiser.bitsToDecimal(self.packet, 2)
        self.dumpFormat["header"]["ancount"] = Bitwiser.bitsToDecimal(self.packet, 3)
        self.dumpFormat["header"]["nscount"] = Bitwiser.bitsToDecimal(self.packet, 4)
        self.dumpFormat["header"]["arcount"] = Bitwiser.bitsToDecimal(self.packet, 5)

    def __setQuestion(self):
        index = 13
        self.dumpFormat["question"] = []
        for i in range(self.dumpFormat["header"]["qdcount"]):
            resource = dict()
            qname = ""
            for index in range(index, len(self.packet)):
                if self.packet[index] == 0: break
                if self.packet[index] < 32:
                    qname += '.'
                    continue
                qname += chr(self.packet[index])
            resource["qname"] = qname
            index += 1
            question = self.packet[index:]
            resource["qtype"] = Bitwiser.bitsToDecimal(question, 0)
            index += 2
            resource["qclass"] = Bitwiser.bitsToDecimal(question, 1)
            index += 2
            self.dumpFormat["question"].append(resource)
        self.answerIndex = index + 1 

    def __setAnswer(self):
        answer = self.packet[self.answerIndex:]
        print(Bitwiser.bitsToDecimal(answer, 0, 16))
