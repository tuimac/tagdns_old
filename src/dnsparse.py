import struct

class DNSParse:
    @staticmethod
    def a(query):
        #id16, qr1, opcode4, aa1, tc1, rd1, ra1, z1, ad1, cd1, rcode4 
        datalist = struct.unpack('', query[:8])
        for x in datalist:
            print(x)
