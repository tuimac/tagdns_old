import binascii

class Packet:
    def dumpAll(packet, digits=16):
        binary = bin(int(binascii.hexlify(packet.strip()), 16)).zfill(8)[2:]
        i = 0
        header_index = 0
        length = len(binary)
        print("[header]")
        while i < length:
            if header_index == 6: print("\n[Question]")
            before = i
            i = i + digits
            print(binary[before:i])
            header_index += 1
