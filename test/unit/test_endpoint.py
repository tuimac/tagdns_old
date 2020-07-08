#!/usr/bin/env python3

from os import path, mkdir
import sys
import time
import traceback
import unittest
import xmlrunner

sys.path.insert(0, path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from tagdns.endpoint import Endpoint

REPORT = path.dirname(path.dirname(path.abspath(__file__))) + '/reports/TEST_tagdns_' + path.basename(__file__).split('.')[0] + '.xml'

class TestEndpoint(unittest.TestCase):
    def test_closeEndpoint(self):
        try:
            endpoint = Endpoint()
            endpoint.daemon = True
            endpoint.start()
            endpoint.closeAllEndpoint()
            time.sleep(1)
        except:
            self.fail(traceback.format_exc())

if __name__ == '__main__':
    if not path.exists(path.dirname(REPORT)):
        mkdir(path.dirname(REPORT))
        with open(REPORT, 'a') as f:
            f.write('')
    with open(REPORT, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
