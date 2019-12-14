#!/usr/bin/env python3

'''
def pickbit(subbyte, start, end, length=8):
    if(start > end): return subbyte
    seed = (subbyte >> (length - start)) << (length - start)
    return (subbyte - seed) >> (length - end - 1)
'''

if __name__ == '__main__':
    #test = ('t', 'e', '')
    test = "10.2.0.8"
    tmp = ""

    for x in test:
        if x == '.' :
            print(int(tmp.encode('ascii'), base=10))
            tmp = ""
            continue
        tmp += x
