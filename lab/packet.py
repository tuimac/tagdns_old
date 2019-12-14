import binascii

class Packet:
    def __printBit():
        binary = bin(int(binascii.hexlify(self.request.strip()), 16)).zfill(8)[2:]
        i = 0
        header_index = 0
        length = len(binary)
        print("[header]")
        while i < length:
            if header_index == 6: print("\n[Question]")
            before = i
            i = i + 16
            print(binary[before:i])
            header_index += 1    
