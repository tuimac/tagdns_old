#!/usr/bin/env python3

from os import path, mkdir
import sys
import time
import traceback
import unittest
import xmlrunner
import timeout_decorator

sys.path.insert(0, path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from tagdns.endpoint import Endpoint

REPORT = path.dirname(path.dirname(path.abspath(__file__))) + '/reports/tagdns_' + path.basename(__file__).split('.')[0] + '.xml'

class TestEndpoint(unittest.TestCase):

    @timeout_decorator.timeout(6)
    def test_closeEndpoint(self):
        try:
            endpoint = Endpoint()
            endpoint.daemon = True
            endpoint.start()
            time.sleep(2)
            endpoint.closeAllEndpoint()
            time.sleep(2)
        except:
            self.fail(traceback.format_exc())

    @timeout_decorator.timeout(6)
    def test_getInboundQueue(self):
        try:
            endpoint = Endpoint()
            endpoint.daemon = True
            endpoint.start()
            time.sleep(2)
            inbound = endpoint.getInboundQueue()
            inbound.put('test')
            self.assertEqual('test', inbound.get())
            endpoint.closeAllEndpoint()
            time.sleep(2)
        except:
            self.fail(traceback.format_exc())

    @timeout_decorator.timeout(6)
    def test_getOutboundQueue(self):
        try:
            endpoint = Endpoint()
            endpoint.daemon = True
            endpoint.start()
            time.sleep(2)
            outbound = endpoint.getOutboundQueue()
            inbound = endpoint.getInboundQueue()
            outbound.put((b'test', ('localhost', 53)))
            self.assertEqual(b'test', inbound.get())
            endpoint.closeAllEndpoint()
            time.sleep(2)
        except:
            self.fail(traceback.format_exc())

if __name__ == '__main__':
    if not path.exists(path.dirname(REPORT)):
        mkdir(path.dirname(REPORT))
        with open(REPORT, 'a') as f:
            f.write('')
    with open(REPORT, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
