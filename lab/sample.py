#!/usr/bin/env python3

import hashlib
import time

if __name__ == '__main__':
    name = "tuimac"
    bitlong = 65535
    
    for i in range(30):
        print(hash(name))
        print(hash(name) & bitlong)
        time.sleep(0.02)
    #database = [] * bitlong
