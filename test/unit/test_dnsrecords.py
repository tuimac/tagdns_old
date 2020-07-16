#!/usr/bin/env python3

from os import path, mkdir
import sys
import socket
import time
import traceback
import unittest
import xmlrunner
import timeout_decorator

sys.path.insert(0, path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from src.dnsrecords import DNSRecords

REPORT = path.dirname(path.dirname(path.abspath(__file__))) + '/reports/tagdns_' + path.basename(__file__).split('.')[0] + '.xml'
PATH = path.dirname(path.abspath(__file__)) + '/sample.json'

class TestDNSRecords(unittest.TestCase):

    @timeout_decorator.timeout(6)
    def test_createRecords(self):
        try:
            records = DNSRecords(PATH)
        except:
            self.fail(traceback.format_exc())

    @timeout_decorator.timeout(6)
    def test_setRecords(self):
        try:
            records = DNSRecords(PATH)
            records['test'] = 0
            with open(PATH, 'r') as f:
                test = json.load(f)
                self.assertEqual(0, test['test'])
        except:
            self.fail(traceback.format_exc())

if __name__ == '__main__':
    if not path.exists(path.dirname(REPORT)):
        mkdir(path.dirname(REPORT))
        with open(REPORT, 'a') as f:
            f.write('')
    with open(REPORT, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
