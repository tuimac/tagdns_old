#!/usr/bin/env python3

from os import path, mkdir
import sys
import time
import traceback
import unittest
import xmlrunner

REPORT = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/reports/tagdns_' + path.basename(__file__).split('.')[0] + '.xml'

class TestDnsQuery(unittest.TestCase):
    def test_query(self):
        pass

    def test_reverseQuery(self):
        pass

if __name__ == '__main__':
    if path.exists(REPORT):
        remove(REPORT)
    if not path.exists(path.dirname(REPORT)):
        mkdir(path.dirname(REPORT))
    with open(REPORT, 'a') as f:
        f.write('')
    with open(REPORT, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
