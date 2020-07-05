#!/usr/bin/env python3

import xmlrunner
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sample.sample import Sample

def main():
    print(sys.path)

if __name__ == "__main__":
    sample = Sample()
