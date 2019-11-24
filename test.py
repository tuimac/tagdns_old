#!/usr/bin/env python3

from dns import Dns

if __name__ == '__main__':
   dns = Dns("localhost", 53)
   dns.run_dns()
