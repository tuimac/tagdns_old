#!/usr/bin/env python3

import unittest

import socket
from dns import resolver, reversename

NAMESERVER = '10.255.0.2'

class TestDnsQuery(unittest.TestCase):
    def test_queryA(self):
        client = resolver.Resolver()
        client.nameserver = [NAMESERVER]
        result = client.query('tagdns','A')
        ipaddress = result.rrset.items[0].address
        
        self.assertEqual(nameserver, ipaddress)

    def test_queryPTR(self):
        ptr = reversename.from_address(NAMESERVER)
        client = resolver.Resolver()
        client.nameserver = [NAMESERVER]
        results = client.query(ptr,'PTR')
        
        self.assertNotEqual(0, results.len())

if __name__ == '__main__':
    unittest.main()
