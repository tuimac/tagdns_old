#!/usr/bin/env python3

from dns import Dns

if __name__ == '__main__':
    stop = True
    dns = Dns("localhost", 53, stop)
    dns.run_dns()
