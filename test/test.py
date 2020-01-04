#!/usr/bin/env python3

class Test(list):
    def __init__(self, testList):
        self.testList = testList

if __name__ == '__main__':
    tmpList = [1] * 10
    test = Test(tmpList)
    test.append(10)
    print(test)
