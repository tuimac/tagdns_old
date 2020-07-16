#!/usr/bin/env python3

import struct
from dnspaarse import DNSParse

if __name__ == '__main__':
    query = (b'8\xf7\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x04test\x06tuimac\x07private\x00\x00\x01\x00\x01', ('172.17.0.2', 55909))
    data = query[0]
    DNSParse.a()
