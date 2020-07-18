#!/usr/bin/env python3

import struct
from dnsparse import DNSParse

if __name__ == '__main__':
    queries = [
        (b'8\xf7\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x04test\x06tuimac\x07private\x00\x00\x01\x00\x01', ('172.17.0.2', 55909)),
        (b'\xc1\xd0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x012\x010\x0217\x03172\x07in-addr\x04arpa\x00\x00\x0c\x00\x01', ('172.17.0.2', 44703)),
    ]
    for query in queries:
        dnsparse = DNSParse(query[0])
