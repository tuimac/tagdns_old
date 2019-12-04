#Reference is below:
# http://www.networksorcery.com/enp/protocol/dns.htm

class Resolver:
    def __init__(self, request):
        self.request = request

    def resolve(self):
        request = self.__parseRequest()
        print(request)

    def __parseRequest(self):
        request = self.request[0]
        request.strip()

        return bin(int(binascii.hexlify(request), 16)).zfill(8)[6:]   
        
