#!/usr/bin/env python3

from dns import resolver, reversename
from os import path, mkdir
import unittest
import socket
import xmlrunner
import traceback
import sys

REPORT = 'reports/tagdns_' + path.basename(__file__).split('.')[0] + '.xml'
NAMESERVER = ''

class TestDnsQuery(unittest.TestCase):
    def test_queryA(self):
        pass
        '''
        client = resolver.Resolver()
        client.nameserver = [NAMESERVER]
        result = client.query('tagdns','A')
        ipaddress = result.rrset.items[0].address
        self.assertEqual(nameserver, ipaddress)
        '''

    def test_queryPTR(self):
        pass
        '''
        ptr = reversename.from_address(NAMESERVER)
        client = resolver.Resolver()
        client.nameserver = [NAMESERVER]
        results = client.query(ptr,'PTR')
        self.assertNotEqual(0, results.len())
        '''

if __name__ == '__main__':
    NAMESERVER = sys.argv[1]
    if not path.exists(path.dirname(REPORT)):
        mkdir(path.dirname(REPORT))
        with open(REPORT, 'a') as f:
            f.write('')
    with open(REPORT, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
