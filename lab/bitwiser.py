import sys

class Bitwiser:
    
    @staticmethod
    def bitsToDecimal(packet, row, start=0, end=-1, length=16):
        if end == -1: end = length - 1
        LEN = 8
        target = 0
        if type(packet) is not bytes:
            print("Packet argument type is wrong.")
            return
        packet = list(packet)
        numOfBytes = int(length / LEN)
        for i in range(row * numOfBytes, row * numOfBytes + numOfBytes):
            target = (target << LEN) + packet[i]
        return (target - ((target >> (length - start)) << (length - start))) >> (length - end - 1)

    @staticmethod
    def flipBit(bits, position, length=8):
        return bits ^ (1 << position)
