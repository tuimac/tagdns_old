import binascii

class Resolver:
    def __init__(self, request):
        self.ip = request[1][0]
        self.port = request[1][1]
        self.request = bin(int(binascii.hexlify(request[0].strip()), 16)).zfill(8)
        #[6:]

    def resolve(self):
        print(self.request)
        pass
