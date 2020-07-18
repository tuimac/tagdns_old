import struct
import json

class DNSParse:
    def __init__(self, query):
        self.query = dict()
        self.query['id'], flags, self.query['qdcount'], self.query['ancount'], self.query['nscount'], self.query['arcount'] = struct.unpack('!HHHHHH', query[:12])
        self.query['qr'] = (flags & 32768) >> 15
        self.query['opcode'] = (flags & 30720) >> 11
        self.query['aa'] = (flags & 1024) >> 10
        self.query['tc'] = (flags & 512) >> 9
        self.query['rd'] = (flags & 256) >> 8
        self.query['ra'] = (flags & 128) >> 7
        self.query['z'] = (flags & 112) >> 4
        self.query['rcode'] = flags & 15
        self.dump()

    def a(self, query):
        datalist = struct.unpack('', query[:8])
        for x in datalist:
            print(x)

    def dump(self):
        print(json.dumps(self.query,
            indent=4,
            separators=(',', ': ')
        ))
