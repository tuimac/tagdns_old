#!/usr/bin/env python3

import os
import sys
import time
import traceback
import unittest
import xmlrunner

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tagdns.endpoint import Endpoint

REPORT = os.path.dirname(os.path.abspath(__file__)) + "/report"

class TestEndpoint(unittest.TestCase):
    def test_closeEndpoint(self):
        try:
            endpoint = Endpoint()
            endpoint.daemon = True
            endpoint.start()
            endpoint.closeAllEndpoint()
        except:
            self.fail(traceback.format_exc())

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=REPORT),
        failfast=False,
        buffer=False,
        catchbreak=False,
        exit=False
    )
